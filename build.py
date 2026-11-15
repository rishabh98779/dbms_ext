#!/usr/bin/env python3
"""Assemble the Unit III study guide HTML and render it to PDF with WeasyPrint."""
import pathlib
import sys
import re

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
ASSETS = ROOT / "assets"
OUT_HTML = ROOT / "Unit_III_Important_Study_Guide.html"
OUT_PDF = ROOT / "Unit_III_Important_Study_Guide.pdf"

PARTS = [
    "00_cover_toc.html",
    "10_part1.html",
    "20_part2.html",
    "30_part3_a.html",
    "31_part3_b.html",
    "32_part3_c.html",
    "33_part3_d.html",
    "40_part4.html",
    "50_part5.html",
]

FOOT = "</body>\n</html>\n"


def inline_css() -> str:
    """Return the stylesheet with fonts embedded as data URIs, so the HTML is standalone."""
    import base64
    css = (ASSETS / "style.css").read_text(encoding="utf-8")
    fonts = ASSETS / "fonts"
    for ttf in sorted(fonts.glob("*.ttf")):
        b64 = base64.b64encode(ttf.read_bytes()).decode("ascii")
        css = css.replace(f"url(fonts/{ttf.name})",
                          f"url(data:font/ttf;base64,{b64})")
    return css


def build_html() -> str:
    css = inline_css()
    head = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Unit III — Practical Study Guide</title>
<style>
{css}
</style>
</head>
<body>
"""
    chunks = [head]
    for name in PARTS:
        path = SRC / name
        text = path.read_text(encoding="utf-8")
        chunks.append(f"\n<!-- ===== {name} ===== -->\n")
        chunks.append(text)
    chunks.append(FOOT)
    return "".join(chunks)


def main() -> int:
    html = build_html()
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"wrote {OUT_HTML} ({len(html):,} chars)")

    from weasyprint import HTML, CSS
    HTML(filename=str(OUT_HTML)).write_pdf(
        str(OUT_PDF), stylesheets=[CSS(filename=str(ASSETS / "style.css"))]
    )
    print(f"wrote {OUT_PDF} ({OUT_PDF.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
