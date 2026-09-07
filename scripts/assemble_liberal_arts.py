#!/usr/bin/env python3
"""Assemble translated fragments into the original liberal arts LaTeX structure.

The Chinese book is one generated LaTeX file. Splitting at its existing book,
part, and chapter boundaries allows independent translation without changing
the typesetting. No new LaTeX includes or formatting commands are introduced.
"""

import argparse
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "literal_arts/latex/literal_book.tex"
TARGET = ROOT / "EN/literal_arts/latex"
BOUNDARY = re.compile(r"^\\(chapter|frontchapter|volumediv|part)\{", re.MULTILINE)


def source_fragments():
    source = SOURCE.read_text(encoding="utf-8")
    boundaries = list(BOUNDARY.finditer(source))
    result = [("preamble.tex", source[:boundaries[0].start()])]
    counters = Counter()
    names = {"chapter": "ch", "frontchapter": "front", "volumediv": "volume", "part": "part"}
    for index, match in enumerate(boundaries):
        kind = match.group(1)
        counters[kind] += 1
        end = boundaries[index + 1].start() if index + 1 < len(boundaries) else len(source)
        name = f"{names[kind]}{counters[kind]:03d}.tex"
        result.append((name, source[match.start():end]))
    assert "".join(content for _, content in result) == source
    assert counters["chapter"] == 114
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extract", type=Path, help="Export Chinese source fragments for translation")
    parser.add_argument("--check", action="store_true", help="Check existing English fragments without assembling")
    args = parser.parse_args()
    fragments = source_fragments()
    if args.extract:
        args.extract.mkdir(parents=True, exist_ok=True)
        for name, content in fragments:
            (args.extract / name).write_text(content, encoding="utf-8")
        print(f"Extracted {len(fragments)} source fragments into {args.extract}")
        return 0

    from check_english import ENVIRONMENT, HEADING, REFERENCE, STYLE, without_comments, normalize_pagination, HAN_EXAMPLES, has_untranslated_han

    translated = []
    missing = []
    errors = []
    for name, original in fragments:
        path = TARGET / "fragments" / name
        if not path.is_file():
            missing.append(name)
            continue
        english = path.read_text(encoding="utf-8")
        source_clean = without_comments(original)
        try:
            english_clean = without_comments(normalize_pagination(english))
        except ValueError as error:
            errors.append(f"{name}: {error}")
            continue
        if not english_clean.strip() or has_untranslated_han(english_clean, source_clean, HAN_EXAMPLES.get(name, ())):
            errors.append(f"{name}: empty or contains Chinese requiring translation/review")
        for pattern in (ENVIRONMENT, HEADING, REFERENCE, STYLE):
            if pattern.findall(source_clean) != pattern.findall(english_clean):
                errors.append(f"{name}: changed LaTeX structure ({pattern.pattern})")
        # A terminal newline separates adjacent structural commands exactly as
        # in the source. Translations should retain paragraph boundaries too.
        translated.append(english.rstrip("\n") + "\n")
    print(f"Liberal arts: {len(translated)}/{len(fragments)} fragments translated")
    if missing:
        print("Missing: " + ", ".join(missing))
    for error in errors:
        print("ERROR: " + error)
    if errors or (missing and not args.check):
        return 1
    if not args.check:
        output = TARGET / "literal_book.tex"
        output.write_text("".join(translated), encoding="utf-8")
        print(f"Assembled {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
