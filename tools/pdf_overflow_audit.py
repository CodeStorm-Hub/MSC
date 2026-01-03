"""PDF layout audit: find content that overflows the page bounds.

This is intended for QA of "Save as PDF" output from HTML, where tables/diagrams
might clip outside the printable area.

Usage:
  python tools/pdf_overflow_audit.py --pdf docs/SRS.pdf

Notes:
- We treat any content bbox outside page.rect as an overflow.
    - Text: via page.get_text("blocks")
    - Images: via page.get_text("dict") blocks of type=1
    - Vector drawings (lines/shapes/diagrams): via page.get_drawings()
- We also report the tightest bounding boxes per page to estimate margins.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

PT_TO_MM = 25.4 / 72.0


@dataclass(frozen=True)
class Overflow:
    page: int
    bbox: Tuple[float, float, float, float]
    page_rect: Tuple[float, float, float, float]
    kind: str
    sample: str


def _bbox_union(
    b1: Optional[Tuple[float, float, float, float]],
    b2: Tuple[float, float, float, float],
) -> Tuple[float, float, float, float]:
    if b1 is None:
        return b2
    x0 = min(b1[0], b2[0])
    y0 = min(b1[1], b2[1])
    x1 = max(b1[2], b2[2])
    y1 = max(b1[3], b2[3])
    return (x0, y0, x1, y1)


def _mm(v: float) -> float:
    return v * PT_TO_MM


def _clip_bbox_to_page(
    bbox: Tuple[float, float, float, float],
    rect: "fitz.Rect",  # type: ignore[name-defined]
) -> Optional[Tuple[float, float, float, float]]:
    """Clip a bbox to a page rect.

    Returns None if there is no intersection.
    """
    x0, y0, x1, y1 = bbox
    cx0 = max(x0, float(rect.x0))
    cy0 = max(y0, float(rect.y0))
    cx1 = min(x1, float(rect.x1))
    cy1 = min(y1, float(rect.y1))
    if cx1 <= cx0 or cy1 <= cy0:
        return None
    return (cx0, cy0, cx1, cy1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a PDF for overflow/clipping outside page bounds.")
    parser.add_argument("--pdf", required=True, help="Path to PDF file")
    parser.add_argument("--tol-pt", type=float, default=0.5, help="Tolerance in points when checking bounds")
    parser.add_argument(
        "--drawing-max-over-pt",
        type=float,
        default=20.0,
        help=(
            "Max allowed drawing overshoot (pt) to treat as a true overflow. "
            "Large overshoots are often clipped multi-page borders and are ignored."
        ),
    )
    parser.add_argument("--max-overflows", type=int, default=40, help="Max overflow items to print")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    try:
        import fitz  # PyMuPDF  # type: ignore[import-not-found]
    except Exception as e:  # pragma: no cover
        raise SystemExit(f"PyMuPDF not available. Install with: python -m pip install PyMuPDF\n{e}")

    doc = fitz.open(str(pdf_path))

    overflows: List[Overflow] = []
    # (page, left, right, top, bottom) in mm
    text_margin_summaries: List[Tuple[int, float, float, float, float]] = []
    content_margin_summaries: List[Tuple[int, float, float, float, float]] = []

    tol = float(args.tol_pt)
    drawing_max_over = float(args.drawing_max_over_pt)

    for i in range(doc.page_count):
        page = doc.load_page(i)
        rect = page.rect  # points
        page_rect = (rect.x0, rect.y0, rect.x1, rect.y1)

        # Text blocks: (x0, y0, x1, y1, "text", block_no, block_type)
        blocks = page.get_text("blocks")

        text_union: Optional[Tuple[float, float, float, float]] = None
        content_union: Optional[Tuple[float, float, float, float]] = None

        for b in blocks:
            x0, y0, x1, y1, text = float(b[0]), float(b[1]), float(b[2]), float(b[3]), str(b[4] or "")
            text_norm = " ".join(text.split())
            if not text_norm:
                continue

            text_union = _bbox_union(text_union, (x0, y0, x1, y1))
            clipped = _clip_bbox_to_page((x0, y0, x1, y1), rect)
            if clipped is not None:
                content_union = _bbox_union(content_union, clipped)

            if (x0 < rect.x0 - tol) or (y0 < rect.y0 - tol) or (x1 > rect.x1 + tol) or (y1 > rect.y1 + tol):
                overflows.append(
                    Overflow(
                        page=i + 1,
                        bbox=(x0, y0, x1, y1),
                        page_rect=page_rect,
                        kind="text",
                        sample=text_norm[:120],
                    )
                )

        # Image blocks (rare in this doc, but can happen)
        try:
            text_dict = page.get_text("dict")
            for block in text_dict.get("blocks", []):
                if int(block.get("type", -1)) != 1:
                    continue
                bbox = block.get("bbox")
                if not bbox or len(bbox) != 4:
                    continue
                x0, y0, x1, y1 = float(bbox[0]), float(bbox[1]), float(bbox[2]), float(bbox[3])
                clipped = _clip_bbox_to_page((x0, y0, x1, y1), rect)
                if clipped is not None:
                    content_union = _bbox_union(content_union, clipped)
                if (x0 < rect.x0 - tol) or (y0 < rect.y0 - tol) or (x1 > rect.x1 + tol) or (y1 > rect.y1 + tol):
                    overflows.append(
                        Overflow(
                            page=i + 1,
                            bbox=(x0, y0, x1, y1),
                            page_rect=page_rect,
                            kind="image",
                            sample="",
                        )
                    )
        except Exception:
            # Some PDFs can fail dict extraction; keep audit best-effort.
            pass

        # Vector drawings (lines/shapes/diagrams). This helps catch clipping from borders/diagrams.
        try:
            drawings = page.get_drawings()
            for d in drawings:
                r = d.get("rect")
                if r is None:
                    continue
                x0, y0, x1, y1 = float(r.x0), float(r.y0), float(r.x1), float(r.y1)
                clipped = _clip_bbox_to_page((x0, y0, x1, y1), rect)
                if clipped is not None:
                    content_union = _bbox_union(content_union, clipped)

                # Drawings can have huge bboxes (e.g., a long table border) but still be clipped
                # at render time. Treat only small overshoots as a real risk.
                left_over = float(rect.x0) - x0
                top_over = float(rect.y0) - y0
                right_over = x1 - float(rect.x1)
                bottom_over = y1 - float(rect.y1)
                max_over = max(left_over, top_over, right_over, bottom_over)
                is_outside = (x0 < rect.x0 - tol) or (y0 < rect.y0 - tol) or (x1 > rect.x1 + tol) or (y1 > rect.y1 + tol)

                if is_outside and max_over <= drawing_max_over:
                    overflows.append(
                        Overflow(
                            page=i + 1,
                            bbox=(x0, y0, x1, y1),
                            page_rect=page_rect,
                            kind="drawing",
                            sample="",
                        )
                    )
        except Exception:
            pass

        if text_union is None:
            text_margin_summaries.append((i + 1, float("nan"), float("nan"), float("nan"), float("nan")))
        else:
            left = _mm(text_union[0] - rect.x0)
            right = _mm(rect.x1 - text_union[2])
            top = _mm(text_union[1] - rect.y0)
            bottom = _mm(rect.y1 - text_union[3])
            text_margin_summaries.append((i + 1, left, right, top, bottom))

        if content_union is None:
            content_margin_summaries.append((i + 1, float("nan"), float("nan"), float("nan"), float("nan")))
        else:
            left = _mm(content_union[0] - rect.x0)
            right = _mm(rect.x1 - content_union[2])
            top = _mm(content_union[1] - rect.y0)
            bottom = _mm(rect.y1 - content_union[3])
            content_margin_summaries.append((i + 1, left, right, top, bottom))

    print(f"PDF: {pdf_path}")
    print(f"Pages: {doc.page_count}")
    print(f"Overflow blocks: {len(overflows)} (tol={tol}pt)")

    pages_with_overflow = sorted({o.page for o in overflows})
    if pages_with_overflow:
        print(f"Pages with overflow: {pages_with_overflow}")
    else:
        print("Pages with overflow: none")

    # Margin overview: show worst (tightest) margins across pages.
    text_finite = [m for m in text_margin_summaries if all(isinstance(v, (int, float)) and v == v for v in m[1:])]
    content_finite = [
        m for m in content_margin_summaries if all(isinstance(v, (int, float)) and v == v for v in m[1:])
    ]

    if text_finite:
        min_left = min(m[1] for m in text_finite)
        min_right = min(m[2] for m in text_finite)
        min_top = min(m[3] for m in text_finite)
        min_bottom = min(m[4] for m in text_finite)
        print(
            "Tightest observed TEXT margins (mm) across all pages: "
            f"left={min_left:.1f}, right={min_right:.1f}, top={min_top:.1f}, bottom={min_bottom:.1f}"
        )

    if content_finite:
        min_left = min(m[1] for m in content_finite)
        min_right = min(m[2] for m in content_finite)
        min_top = min(m[3] for m in content_finite)
        min_bottom = min(m[4] for m in content_finite)
        print(
            "Tightest observed CONTENT margins (mm) across all pages: "
            f"left={min_left:.1f}, right={min_right:.1f}, top={min_top:.1f}, bottom={min_bottom:.1f}"
        )

    # Print per-page margins for first few + any suspiciously tight pages.
    # Threshold: < 8mm is usually risky for A4 PDF printing.
    risky_threshold_mm = 8.0
    # Use text margins for risk by default (graphics can legitimately run wider).
    risky = [m for m in text_finite if any(v < risky_threshold_mm for v in m[1:])]

    def _fmt(m: Tuple[int, float, float, float, float]) -> str:
        p, l, r, t, b = m
        return f"p{p:03d}: L {l:.1f}mm | R {r:.1f}mm | T {t:.1f}mm | B {b:.1f}mm"

    print("\nPer-page margin summary (mm):")
    for m in text_finite[:5]:
        print("  ", _fmt(m))

    if len(text_finite) > 5:
        print("  ...")

    if risky:
        print(f"\nPages with any margin < {risky_threshold_mm:.1f}mm:")
        for m in risky[:30]:
            print("  ", _fmt(m))
        if len(risky) > 30:
            print(f"  ... ({len(risky) - 30} more)")

    if overflows:
        print("\nSample overflow items:")
        for o in overflows[: int(args.max_overflows)]:
            x0, y0, x1, y1 = o.bbox
            pr = o.page_rect
            print(
                f"  p{o.page:03d} [{o.kind}] bbox=({x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f}) page=({pr[0]:.1f},{pr[1]:.1f},{pr[2]:.1f},{pr[3]:.1f})"
            )
            if o.sample:
                print(f"    sample: {o.sample}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
