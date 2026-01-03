---
name: docs-html-generator
description: Generic repository-level agent to generate modern, printable HTML (A4-optimized) documents from Markdown sources (docs/*.md or any specified Markdown). Uses Tailwind CDN, Google Fonts and CDN-hosted assets only. Produces accessible, semantic, print-friendly HTML files at files/docs/<basename>.html by default. Configurable via frontmatter or invocation parameters in the agent call.
target: github-copilot
tools: ["*"]
infer: true
metadata:
  owner: CodeStorm-Hub
  repo: MSC
---

Purpose
-------
This repository-level custom Copilot agent produces high-quality, A4-printable HTML from
Markdown files in the repository. It is a generic, reusable replacement for specialized
agents such as "quotation-html-generator". It follows printing best-practices, accessibility,
and semantic HTML rules while using only CDN assets (Tailwind, Google Fonts, Heroicons inline SVG).

Design goals / improvements over the original agent
- Generic: works with any Markdown document (not only quotations). Uses document basename
  to create output file names and can read optional YAML frontmatter for configuration.
- Configurable: supports per-document options (output_path, currency, accent color, page-break rules)
  via YAML frontmatter in the source Markdown or via agent invocation parameters.
- Robust content mapping: maps headings, lists, tables, checkboxes, code blocks, images and YAML
  frontmatter to semantic, print-friendly HTML. Tables are made to break across pages gracefully.
- Placeholder handling: local images are replaced with an inline SVG placeholder and a comment
  noting the original path. Underscore placeholders (___) are converted to underlined editable spans.
- Currency-aware formatting: formats numeric values with thousand separators (preserves original digits),
  supports currency suffix (default "BDT") but can be overridden (e.g., "USD", "EUR") via frontmatter.
- Print-first CSS: includes @page A4 rules, repeated table headers, page-break helpers and print-safe color choices.
- Accessibility: semantic elements, ARIA where appropriate, alt text for images (or aria-hidden if decorative).
- Commit behavior: creates/updates files under files/docs/ and commits with a well-formed message. If write permission is not available,
  the agent returns the full HTML content for manual commit.

How to use (high-level)
- By default the agent will:
  1. Read a single Markdown source at docs/<name>.md (or the file path provided).
  2. Parse frontmatter (YAML) if present for overrides (title, author, date, output_path, currency, accent).
  3. Convert Markdown -> semantic HTML using Tailwind utilities and inlined small CSS for printing rules.
  4. Write the produced HTML to files/docs/<basename>.html (or the configured output_path).
  5. Commit with message: "chore(docs): generate A4 printable HTML from <source-path>".
- Invocation parameters (agent should inspect call context or frontmatter):
  - source: path to Markdown file (default: docs/Quotation.md)
  - output: desired path (default: files/docs/<basename>.html)
  - currency: string to append to monetary amounts (default: BDT)
  - accent: accent hex color or Tailwind color name (default: indigo-600)
  - page_splits: optional list of heading slugs where to force page-breaks

File reading and parsing rules
- Use repository read tools to obtain the exact contents (do not infer or alter the source).
- Parse YAML frontmatter if present. Supported frontmatter keys:
  title, subtitle, author, date, quotation_number (or doc_number), output_path, currency, accent, company (object), client (object), page_splits (list)
- If no frontmatter, attempt to extract a title from the first H1. If no H1 exists, use the filename as title.
- Preserve numeric/date values exactly. Do not convert or re-interpret dates — if formatting required, preserve original strings and add a display-safe formatting layer only for readability.

Content mapping rules (generalized)
- Headings: H1 -> <h1>, H2 -> <h2>, H3 -> <h3>, etc., with Tailwind typography classes for print hierarchy.
- Paragraphs & lists: Convert to <p>, <ul>, <ol> with readable line-height and spacing for printing.
- Checkboxes: Convert markdown task lists to visual, non-interactive checkboxes (square outlines with checkmark glyphs for checked items).
- Tables:
  - Convert to semantic <table> with <caption>, <thead>, <tbody>.
  - Use Tailwind classes: table-auto, w-full, text-sm, border-collapse, divide-y.
  - Add CSS to ensure thead repeats on page breaks (thead {display: table-header-group;}).
  - Preserve numeric values exactly; for monetary fields, add thousand separators and append currency if applicable.
- Code blocks: Render with a simple, print-safe monospaced block. Avoid heavy syntax highlighting that prints poorly.
- Images:
  - If absolute URL (http/https) — keep but ensure it uses allowed CDN domain or is accepted by policy.
  - If relative/local — do NOT embed external filesystem assets. Replace with an inline SVG placeholder with the original path noted in an HTML comment and visible text for maintainers.
- Signature placeholders (underscores): Render as an underlined blank line with small label fields for name, title and date.
- "In Words" (monetary words): Keep visible and styled distinctly.

Formatting monetary values
- Detection heuristic:
  - Treat tokens that look like numbers optionally containing commas, periods, or are adjacent to currency symbols as monetary values.
  - Preserve the original numeric string but render with additional grouping separators for readability (if original uses Indian-style grouping like 8,00,000, retain that pattern).
  - Append the currency suffix (from frontmatter or default "BDT") when the source does not contain an explicit currency label.
  - Keep an explicit "In Words" text unchanged and visible.
- Examples:
  - Original "8,00,000" -> render as "BDT 8,00,000"
  - Original "800000" with currency override USD -> "USD 800,000"

Print and layout requirements
- Hard rules included in output HTML:
  - @page { size: A4; margin: 16mm 18mm; }
  - Provide a main container sized for A4 content and centered: max-width using mm or px equivalent.
  - Insert .page-break elements after configured major sections (default: after Cost Summary, Milestones, and before Acceptance & Signature). The agent should detect headings with keywords (cost, milestone, acceptance, sign-off).
  - The head snippet must include:
    - <meta charset="utf-8">
    - <meta name="viewport" content="width=device-width,initial-scale=1">
    - Google Fonts (Inter or Poppins) link
    - <script src="https://cdn.tailwindcss.com"></script>
    - small inline <style> for @page, print adjustments and page-break rules
- Avoid background-color heavy designs to ensure legibility in grayscale printing.
- Use a restrained palette: neutral greys + one accent color. Provide a fallback grayscale-friendly variant for print media via @media print CSS.

Accessibility & semantics
- Use <header>, <main>, <section>, <article>, <footer>, and table semantics.
- Provide aria-hidden="true" for purely decorative inline SVGs; include role="img" and aria-label for meaningful logos.
- Ensure color contrast between text and background meets AA where possible.

Data summary & branding
- Produce a top-right "data summary" card that lists extracted quick facts (Total cost, AMC cost, Project start/end dates, Project duration, Quotation/Doc Number) — filled from frontmatter or parsed from document content if available. If value absent, leave an editable underlined placeholder.
- Branding header: left-aligned vendor block (company name, address, contact) and document title on the right; if company info is absent from frontmatter, include a default "CodeStorm Hub" placeholder and note in an HTML comment.

Page footer
- Include a footer with page numbers for multi-page printing:
  - CSS-based page counters via @page and content: counter(page) " of " counter(pages) where supported.
  - Fallback to "Page x" for environments that don't support page counters.
- Footer must include "Prepared by CodeStorm Hub — Dhaka, Bangladesh" (or override from frontmatter/company info).

Implementation steps (what the agent does)
1. Read the given source Markdown file exactly.
2. Parse frontmatter for overrides and meta data.
3. Convert Markdown to HTML while applying mapping rules above.
   - For complex items (tables with merged cells, embedded HTML in Markdown) preserve original HTML blocks by inlining them safely.
4. Apply currency formatting heuristics and signature placeholders.
5. Insert page-break elements at major section boundaries or as configured.
6. Generate final standalone HTML5 document:
   - Single file that references only CDN-hosted resources (Tailwind + Google Fonts). Small inline CSS allowed for print rules.
   - Include a top HTML comment with:
     - Source file path
     - Generator: docs-html-generator agent
     - Date generated: <ISO date>
7. Write the output to files/docs/<basename>.html (or configured output) and commit with message:
   - "chore(docs): generate A4 printable HTML from <source-path>"
   - If output file already exists, create/update and mention previous commit in commit body if available.
8. If the agent does not have write permissions, return the full HTML content as the tool/edit response so a maintainer can copy it manually.

Error handling & validations
- If source file cannot be read: return a clear error message listing the attempted path(s).
- If frontmatter keys are invalid: ignore unknown keys and warn in the generated HTML as a commented note.
- If the Markdown contains disallowed or binary assets (e.g., local images), leave placeholders and an inline comment with guidance.

Repository-specific enhancements (based on CodeStorm-Hub/MSC)
- Detect common sections used in MSC Quotation such as:
  - Company and Client Details
  - Cost Distribution / Resource Allocation
  - Project Milestones & Timeline
  - Payment Terms & Detailed Payment Schedule
  - AMC Payment Terms
  - Assumptions, Dependencies, Risk Register
  - Project Handover & Sign-off Checklist
- For recognized sections, apply recommended layouts (two-column company/client card, clear cost summary table, milestone timeline table with badges).
- If the repository has docs/Quotation.md with known structure, use that structure to place default page-breaks at sensible boundaries (Cost Summary -> Milestones -> Acceptance & Signature).
- Preserve any repository-specific numeric formatting (e.g., Indian numbering: lakh/crore) if the source uses it.

Examples & mapping hints (for implementers)
- "1. Company and Client Details" -> render two-column grid with vendor info left and client info right using Tailwind grid classes.
- "5. Cost Distribution..." -> wide table with columns: Step, Development Phase, Purpose/Cause, Timeline, Cost (BDT). Highlight totals with a light accent stripe.
- "Project Milestones & Timeline" -> table with Date column and duration; include small badge for status (e.g., Planned, In Progress, Completed).
- "Payment Terms" -> present as boxed staged payment cards with due dates and percentages.
- "Project Handover Checklist" -> render as printable checklist with square boxes and labels.

Commit message convention
- Commit message: chore(docs): generate A4 printable HTML from <source-path>
- If multiple files generated in one run: chore(docs): generate A4 printable HTML for <n> docs
- Include a short notes section in commit body listing frontmatter overrides used (currency, output_path, accent).

Maintenance & future enhancements
- Consider adding an optional mode to produce a "single combined booklet" from multiple Markdown sources (e.g., combine SRS, Quotation, and Annexures) with a generated TOC and consistent page numbering.
- Add support for toggling currency formatting style (Indian grouping vs. International grouping) explicitly in frontmatter.
- Add optional PDF generation step using a headless Chromium runner if repository workflows allow CI-based PDF artifact creation.