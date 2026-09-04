#!/usr/bin/env python3
"""Validate the structural contract for a native interactive HTML presentation."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class PresentationParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.slide_elements = 0
        self.full_slide_images: list[str] = []
        self.has_style = False
        self.has_script = False
        self.has_viewport = False
        self.presentation_slide_count: int | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        classes = set(values.get("class", "").split())

        if tag == "style":
            self.has_style = True
        elif tag == "script":
            self.has_script = True
        elif tag == "meta":
            meta_name = values.get("name", "").lower()
            if meta_name == "viewport":
                self.has_viewport = True
            elif meta_name == "presentation-slide-count":
                try:
                    self.presentation_slide_count = int(values.get("content", ""))
                except ValueError:
                    self.presentation_slide_count = None

        if "slide" in classes and tag in {"article", "section", "div"}:
            self.slide_elements += 1

        if tag == "img":
            src = values.get("src", "")
            alt = values.get("alt", "")
            suspicious_class = classes & {"slide-image", "slide-render", "rendered-slide"}
            suspicious_name = re.search(r"(?:^|[/_-])slide[-_ ]?\d+\.(?:png|jpe?g|webp)(?:$|[?#])", src, re.I)
            suspicious_alt = re.fullmatch(r"\s*slide\s+\d+\s*", alt, re.I)
            if suspicious_class or suspicious_name or suspicious_alt:
                self.full_slide_images.append(src or alt or "unnamed image")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("--min-slides", type=int, default=1)
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    if args.html.suffix.lower() not in {".html", ".htm"}:
        errors.append("Output must use an .html or .htm extension.")
    if not args.html.is_file():
        errors.append(f"File does not exist: {args.html}")
        print("FAILED\n- " + "\n- ".join(errors), file=sys.stderr)
        return 1

    source = args.html.read_text(encoding="utf-8")
    document = PresentationParser()
    try:
        document.feed(source)
    except Exception as exc:  # HTMLParser is lenient; parsing errors are still actionable.
        errors.append(f"HTML parsing failed: {exc}")

    slide_count = max(document.slide_elements, document.presentation_slide_count or 0)

    if slide_count < args.min_slides:
        errors.append(
            f"Found or declared {slide_count} native slides; expected at least {args.min_slides}. "
            "For JS-rendered decks add <meta name=\"presentation-slide-count\" content=\"N\">."
        )
    if document.full_slide_images:
        errors.append(
            "Detected probable rendered slide images: " + ", ".join(document.full_slide_images[:5])
        )
    if not document.has_viewport:
        errors.append("Missing responsive viewport meta tag.")
    if not document.has_style:
        errors.append("Missing embedded CSS <style> block.")
    if not document.has_script:
        errors.append("Missing JavaScript <script> block for presentation interaction.")

    lower = source.lower()
    if "requestfullscreen" not in lower:
        warnings.append("No Fullscreen API usage detected.")
    if "keydown" not in lower:
        errors.append("No keyboard navigation handler detected.")
    if ":hover" not in lower or "focus-visible" not in lower:
        errors.append("Missing hover or visible keyboard-focus styling.")
    if "data-tip" not in lower and "<title>" not in lower:
        warnings.append("No chart/data tooltip hooks detected.")
    if "@media print" not in lower:
        warnings.append("No print stylesheet detected.")

    if errors:
        print("FAILED")
        for error in errors:
            print(f"- {error}")
        for warning in warnings:
            print(f"- WARNING: {warning}")
        return 1

    print(f"PASSED: {args.html} ({slide_count} slides found or declared)")
    for warning in warnings:
        print(f"WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
