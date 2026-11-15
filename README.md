# Unit III — Practical Study Guide (DBMS)

A condensed, high-yield revision handbook built from `Part 3.docx`, the Unit III
practical question bank (86 questions across four sections, Batches 1–4).

The goal is not to reproduce the source document but to curate it: keep the
academically valuable material, merge repetitive questions, and present it as a
clean 35-page PDF study guide.

## Contents

| File | Description |
| --- | --- |
| `Unit_III_Important_Study_Guide.pdf` | The finished study guide (35 pages, A4) |
| `Unit_III_Important_Study_Guide.html` | Editable, self-contained source (fonts embedded) |
| `Part 3.docx` | Original source document |
| `build.py` | Builds the HTML and PDF from the partials |
| `src/*.html` | Content partials (cover/TOC, Parts 1–5, accuracy notes) |
| `assets/style.css` | Print/design system |
| `assets/fonts/` | Inter font family used by the stylesheet |

## Guide structure

- **Part 1 — Essential Concepts**: plain-language explanations of Sections A–D.
- **Part 2 — Important Formulas & Rules**: cost models, schedule classes, locking,
  timestamp/optimistic rules, recovery rules — each with variables and an example.
- **Part 3 — Important Questions & Solutions**: representative problems by original
  ID (`U3-A-01` … `U3-D-27`) with difficulty and platform tags.
- **Part 4 — Essential SQL Reference**: MySQL 8.0 vs Oracle side-by-side.
- **Part 5 — Last-Minute Revision**: definitions, formula sheet, difference table,
  rules checklist, common traps and a priority question list.

Every question ID from the source is represented. Duplicate questions are folded
into "Related" notes on the primary card, so no concept is dropped.

## Build

Requires Python with `weasyprint` (and `python-docx` only if you re-parse the source):

```bash
pip install weasyprint
python3 build.py
```

This writes `Unit_III_Important_Study_Guide.html` and
`Unit_III_Important_Study_Guide.pdf`.

## Accuracy notes

No question, SQL statement or expected output was invented. SQL was **not executed**
during curation — the source document's own honesty note about this is preserved in
the guide. Platform differences (MySQL vs Oracle) are kept distinct throughout.
Source inconsistencies are flagged in the final section of the guide.
