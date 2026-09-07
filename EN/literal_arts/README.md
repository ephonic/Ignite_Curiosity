# Igniting the Liberal Arts Spark

*A Humanities Tour for Middle School Students*

English translation of the [Chinese liberal arts edition](../../literal_arts/README.md),
in three volumes and 114 chapters. Translation is in progress; no complete
English PDF is published yet.

The document class, fonts, packages, heading styles, volume-page macros, and
table column styles are retained. Prose and visible labels are translated.
With the contributor's approval, oversized tables may be divided at row
boundaries with repeated headers so that content is not clipped by page edges.
The recurring-objects table in `fragments/front004.tex`, thinking-tools
table in `fragments/front005.tex`, and empire comparison in `fragments/ch034.tex`
use this pagination fix. All original rows and column specifications remain.
Their precisely marked, allowlisted boundaries are checked separately rather than
being mistaken for a change to the book's content structure.
See [the English editions README](../README.md) for the exact Chinese source
commit and the incremental-update workflow.

## Sources and building

The Chinese edition's generated `latex/literal_book.tex` is the translation
source. Its English counterpart is maintained as fragments at the original
chapter, part, volume, and front/back-matter boundaries. Assembly joins those
fragments without introducing new LaTeX includes or changing their order.

From the repository root:

```sh
python3 scripts/assemble_liberal_arts.py
python3 scripts/check_english.py literal_arts
python3 scripts/build_english.py literal_arts --publish
```

The builder requires Tectonic, validates the complete sources and compiler log,
and places `Igniting_the_Liberal_Arts_Spark.pdf` beside this README. XeLaTeX
also works on the assembled `latex/literal_book.tex`; Fandol fonts are supplied
by the TeX distribution. Compiler checks must be followed by visual PDF review.

During development, `python3 scripts/assemble_liberal_arts.py --check` validates
only the available fragments and reports missing ones. A build with `--preview`
assembles available material in a temporary build directory and never publishes
an incomplete PDF here.

## Source notes

The original editorial plan and proposed appendices are included as written;
they have not been turned into newly authored supplementary material. Source
inconsistencies are not silently resolved: for example, chapter 1 refers to
the following “twenty-odd chapters,” although the complete book has 114 chapters.

The original series discloses AI-generated text. This translation preserves its
arguments and examples; it does not independently establish the accuracy of
every historical attribution or cultural generalization.
See [source review notes](SOURCE_NOTES.md) for specific review points and
documented pagination changes.
