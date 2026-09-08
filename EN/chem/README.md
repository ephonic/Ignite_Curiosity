# Igniting the Chemistry and Biology Spark

English translation of the [Chinese chemistry and biology edition](../../chem/README.md),
in three volumes. All 87 chapters and six appendices are translated.

The complete [English PDF](Igniting_the_Chemistry_and_Biology_Spark.pdf)
contains 1,054 pages, including the original front matter and all three volumes.

The original document class, fonts, geometry, packages, colored boxes, table
column definitions, and diagram styles are retained. Prose and printed labels
are translated. See [the English editions README](../README.md) for the Chinese
source commit and the incremental-update workflow.

## Build and verification

From the repository root, with Tectonic installed:

```sh
python3 scripts/check_english.py chem
python3 scripts/build_english.py chem --publish
```

The build checks the combined `book.tex` and all three standalone entrypoints,
`vol1.tex`, `vol2.tex`, and `vol3.tex`. After source and log checks, it places
the combined `Igniting_the_Chemistry_and_Biology_Spark.pdf` beside this README,
mirroring the Chinese edition. The build uses the XeTeX engine; the original
XeLaTeX workflow also works from `latex/`. The preamble requires the original
Noto Serif CJK SC, Noto Sans CJK SC, and Noto Sans Mono CJK SC fonts.

Release checks passed for all 103/103 source files and all four entrypoints:
no missing inputs, missing glyphs, unresolved references, or overfull boxes.
Standalone volumes contain 394, 309, and 357 pages respectively. As in the
Chinese directory, only the combined PDF is committed; the three standalone
PDFs can be regenerated with the same build command.

Rendered review covered the contents, revised headings and diagrams, tables,
appendix transitions, and closing pages. A full-page text-bounds and
overlapping-word scan also passed. Compilation and layout review do not
constitute independent scientific verification.

## Layout repairs

English labels and long table cells are wrapped, with local label placement
adjusted where needed. Chapter and appendix titles have explicit line breaks;
the full titles remain in the contents. No table rows or columns were removed,
and the appendix reference tables fit without splitting across pages.

The peptide equation in Chapter 48 occupies two lines without changing any
chemical terms. Chapter 53's unsupported tilde glyph uses the existing math
font instead. Formula inventories were compared before and after layout edits.

Two source typesetting issues are explicitly repaired: Chapter 5's dashed
return arrows now curve below their labels, preserving endpoints and direction;
and `book.tex`/`vol3.tex` place `\backmatter` after the appendices, restoring
A--F numbering and section-counter resets. All other plotted paths and scales
are retained. The combined contents has a wider page-number box for four-digit
numbers; its fonts and leader style remain unchanged.

## Source and safety notes

The original series discloses AI-generated text. Translation is not scientific
or safety validation. Some source numerical comparisons and explanatory claims
are inconsistent: for example, chapters 5 and 6 contain spelled-out large
numbers that disagree with nearby powers of ten. Scientific claims and formulas
are retained rather than silently revised; the presentation-only repairs above
do not correct those source claims.

Chapter 4 also includes a fever-treatment claim involving alcohol rubbing.
That passage is a source claim, not medical guidance from this translation.
Contributor-approved “Translator safety note” paragraphs now warn against this
and other hazardous source advice beside the relevant passages. They cite safety
guidance while leaving the original translated claims visible and styles intact.
The edition's experiments and health-related statements require independent
safety review; do not use this book as a medical or laboratory safety manual.
Read the translated safety front matter before considering any activity.
See [source review notes](SOURCE_NOTES.md) for chapter-specific issues.
