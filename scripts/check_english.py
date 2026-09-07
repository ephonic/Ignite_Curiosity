#!/usr/bin/env python3
"""Check English source coverage and preservation of LaTeX structure.

The default check requires every source file in the selected books. --partial
checks existing translations while explicitly reporting incomplete coverage.
This is a structural check, not a substitute for translation or PDF review.
"""

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOKS = ("math", "phy", "chem", "literal_arts")
HAN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
# Explicit, source-present glyph examples are necessary when a chapter explains
# character shapes. Only these exact boxed examples are exempt from the prose
# translation check; they are NOT removed from structural/style comparison.
HAN_EXAMPLES = {
    "ch014.tex": ("日", "山", "妈", "女", "马", "铜", "钅", "同", "喷嚏", "嚏"),
    "ch032.tex": ("卜",),
    "ch036.tex": ("習", "羽"),
}
ENVIRONMENT = re.compile(r"\\(begin|end)\{([^{}]+)\}")
REFERENCE = re.compile(r"\\(label|ref|eqref|pageref|include|input)\{([^{}]+)\}")
HEADING = re.compile(r"\\(chapter|section|subsection|subsubsection|part)(\*?)\s*[\[{]")
STYLE = re.compile(
    r"\\(?:documentclass|usepackage)(?:\[[^\]]*\])?\{[^{}]*\}"
    r"|\\(?:geometry|setmainfont|setsansfont|setmonofont|setCJKmainfont|"
    r"setCJKsansfont|setCJKmonofont)(?:\[[^\]]*\])?\{[^{}]*\}"
    r"|\\definecolor\{[^{}]*\}\{[^{}]*\}\{[^{}]*\}"
)

# User-approved pagination adds only this exact repeated table boundary/header.
# Remove it for structural comparison, never arbitrary marked text. This also
# works in the assembled liberal-arts entrypoint. Fonts and column styles stay
# unchanged, and every original row remains subject to the normal checks.
PAGINATION_BLOCKS = {
    "recurring-objects": (
        "\\bottomrule\n\\end{tabularx}\n\n"
        "\\begin{tabularx}{\\linewidth}{llX}\n\\toprule\n"
        "Object & First seen & Later connections \\\\\n\\midrule\n"
    ),
    "thinking-tools": (
        "\\bottomrule\n\\end{tabularx}\n\n"
        "\\begin{tabularx}{\\linewidth}{llX}\n\\toprule\n"
        "Tool & First use & Main use \\\\\n\\midrule\n"
    ),
    "empire-comparison": (
        "\\bottomrule\n\\end{tabularx}\n\n"
        "\\begin{tabularx}{\\linewidth}{llllX}\n\\toprule\n"
        "Empire & Money & \\shortstack[l]{Appoint-\\\\ments} & "
        "\\shortstack[l]{Routes and\\\\language} & Approach to difference \\\\\n"
        "\\midrule\n"
    ),
}
PAGINATION = re.compile(
    r"^% EN-PAGINATION-BEGIN ([a-z-]+)\n(.*?)"
    r"^% EN-PAGINATION-END \1\n", re.MULTILINE | re.DOTALL
)


def normalize_pagination(text):
    def remove_verified_block(match):
        name, content = match.groups()
        if name not in PAGINATION_BLOCKS or content != PAGINATION_BLOCKS[name]:
            raise ValueError(f"unrecognized or modified pagination block: {name}")
        return ""
    normalized = PAGINATION.sub(remove_verified_block, text)
    if "EN-PAGINATION-" in normalized:
        raise ValueError("malformed pagination marker")
    return normalized


def without_comments(text):
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def has_untranslated_han(text, source, allowed=()):
    for example in allowed:
        if example in source:
            text = text.replace("\\mbox{" + example + "}", "")
    return bool(HAN.search(text))


def check_book(book, partial):
    source_dir = ROOT / book / "latex"
    target_dir = ROOT / "EN" / book / "latex"
    sources = sorted(source_dir.rglob("*.tex"))
    missing = []
    errors = []
    translated = 0
    for source in sources:
        relative = source.relative_to(source_dir)
        target = target_dir / relative
        if not target.is_file():
            missing.append(str(relative))
            continue
        translated += 1
        original = without_comments(source.read_text(encoding="utf-8"))
        name = str(target.relative_to(ROOT))
        try:
            english = without_comments(normalize_pagination(target.read_text(encoding="utf-8")))
        except ValueError as error:
            errors.append(f"{name}: {error}")
            continue
        if not english.strip():
            errors.append(f"{name}: empty translation")
        allowed = tuple(example for examples in HAN_EXAMPLES.values() for example in examples) if book == "literal_arts" else ()
        if has_untranslated_han(english, original, allowed):
            errors.append(f"{name}: contains untranslated Chinese; review any intentional quotations")
        for label, pattern in (
            ("environment sequence", ENVIRONMENT),
            ("reference/include identifiers", REFERENCE),
            ("heading sequence", HEADING),
            ("document/package/font/color settings", STYLE),
        ):
            if pattern.findall(original) != pattern.findall(english):
                errors.append(f"{name}: changed {label}")
    print(f"{book}: {translated}/{len(sources)} LaTeX files present")
    if missing:
        print("  MISSING: " + ", ".join(missing))
        if not partial:
            errors.append(f"{book}: edition is incomplete")
    for error in errors:
        print("  ERROR: " + error)
    return not errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("books", nargs="*", help="Books to check (default: all four)")
    parser.add_argument("--partial", action="store_true", help="Allow missing files during translation")
    parser.add_argument("--log", type=Path, help="Also reject missing sources or unresolved references in a build log")
    args = parser.parse_args()
    selected = args.books or BOOKS
    if any(book not in BOOKS for book in selected):
        parser.error("books must be chosen from: " + ", ".join(BOOKS))
    results = [check_book(book, args.partial) for book in selected]
    if args.log:
        log = args.log.read_text(encoding="utf-8", errors="replace")
        failures = re.findall(
            r"^.*(?:No file .*\.tex|Missing character:|Undefined control sequence|"
            r"LaTeX Error:|(?:Reference|Citation) .* undefined|"
            r"There were undefined references).*$", log, flags=re.MULTILINE
        )
        if failures:
            print("BUILD ERRORS:\n" + "\n".join(failures))
            results.append(False)
    if args.partial:
        print("PARTIAL CHECK ONLY: this does not certify a complete English edition.")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
