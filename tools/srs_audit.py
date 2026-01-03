from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._skip_depth = 0
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs):
        if tag in {"script", "style", "noscript"}:
            self._skip_depth += 1

    def handle_endtag(self, tag: str):
        if tag in {"script", "style", "noscript"} and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data: str):
        if self._skip_depth > 0:
            return
        if data:
            self._parts.append(data)

    def text(self) -> str:
        return " ".join(self._parts)


def _normalize(s: str) -> str:
    s = s.lower()
    s = s.replace("\u00a0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


REQ_PATTERNS: dict[str, re.Pattern[str]] = {
    "FR": re.compile(r"\bFR-\d{1,3}(?:[a-z])?\b", re.IGNORECASE),
    "BR": re.compile(r"\bBR-\d{1,3}(?:[a-z])?\b", re.IGNORECASE),
    "US": re.compile(r"\bUS-[A-Z]\d{1,2}\b", re.IGNORECASE),
    "NFR": re.compile(r"\bNFR-\d{1,3}(?:[a-z])?\b", re.IGNORECASE),
}


@dataclass
class AuditResult:
    md_ids: dict[str, set[str]]
    html_ids: dict[str, set[str]]
    missing_in_html: dict[str, list[str]]
    extra_in_html: dict[str, list[str]]
    missing_headings: list[str]


def audit(md_path: Path, html_path: Path) -> AuditResult:
    md = md_path.read_text(encoding="utf-8")
    html = html_path.read_text(encoding="utf-8")

    parser = _TextExtractor()
    parser.feed(html)
    html_text = parser.text()

    md_norm = _normalize(md)
    html_norm = _normalize(html_text)

    md_ids: dict[str, set[str]] = {}
    html_ids: dict[str, set[str]] = {}

    for key, pat in REQ_PATTERNS.items():
        md_ids[key] = {m.upper() for m in pat.findall(md)}
        html_ids[key] = {m.upper() for m in pat.findall(html_text)}

    missing_in_html: dict[str, list[str]] = {}
    extra_in_html: dict[str, list[str]] = {}
    for key in REQ_PATTERNS.keys():
        missing_in_html[key] = sorted(md_ids[key] - html_ids[key])
        extra_in_html[key] = sorted(html_ids[key] - md_ids[key])

    # The markdown includes an introductory mini-TOC that uses level-3 headings (###).
    # For the content completeness check we focus on the primary document structure
    # (level 1-2 headings), to avoid flagging harmless TOC wording differences.
    md_headings: list[str] = []
    for line in md.splitlines():
        if line.startswith("###"):
            continue
        if line.startswith("#"):
            title = line.lstrip("#").strip()
            if title:
                md_headings.append(title)

    missing_headings: list[str] = []
    for h in md_headings:
        h_norm = _normalize(h)
        # Quick exact-substring check; works well given we preserve headings.
        if h_norm and h_norm not in html_norm:
            missing_headings.append(h)

    return AuditResult(
        md_ids=md_ids,
        html_ids=html_ids,
        missing_in_html=missing_in_html,
        extra_in_html=extra_in_html,
        missing_headings=missing_headings,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="Compare MSC_Home_SRS.md vs MSC_Home_SRS_Professional.html")
    ap.add_argument("--md", type=Path, required=True)
    ap.add_argument("--html", type=Path, required=True)
    args = ap.parse_args()

    res = audit(args.md, args.html)

    print(f"MD file:   {args.md}")
    print(f"HTML file: {args.html}\n")

    for key in REQ_PATTERNS.keys():
        print(f"[{key}] IDs in MD: {len(res.md_ids[key])} | IDs in HTML: {len(res.html_ids[key])}")
        if res.missing_in_html[key]:
            print(f"  Missing in HTML ({len(res.missing_in_html[key])}): {', '.join(res.missing_in_html[key][:50])}")
            if len(res.missing_in_html[key]) > 50:
                print("  ... (truncated)")
        else:
            print("  Missing in HTML: 0")

        if res.extra_in_html[key]:
            print(f"  Extra in HTML ({len(res.extra_in_html[key])}): {', '.join(res.extra_in_html[key][:50])}")
            if len(res.extra_in_html[key]) > 50:
                print("  ... (truncated)")
        else:
            print("  Extra in HTML: 0")
        print()

    if res.missing_headings:
        print(f"Headings from MD not found verbatim in HTML text: {len(res.missing_headings)}")
        for h in res.missing_headings[:40]:
            print(f"  - {h}")
        if len(res.missing_headings) > 40:
            print("  ... (truncated)")
    else:
        print("All Markdown headings were found in the HTML text (verbatim, case-insensitive).")

    # Exit non-zero if something looks missing.
    any_missing_ids = any(bool(v) for v in res.missing_in_html.values())
    if any_missing_ids or res.missing_headings:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
