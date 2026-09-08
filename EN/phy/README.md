# Igniting the Physics Spark

English translation of the [Chinese physics edition](../../phy/README.md).
All 61 source chapters are translated.

[Read the compiled English PDF](Igniting_the_Physics_Spark.pdf) (783 pages).

The original document class, fonts, geometry, packages, colored boxes, and
diagram styles are retained. Prose and visible labels are translated. Short
running titles, label wrapping, and local label placement prevent English text
from colliding; the plotted paths, shapes, scales, and mathematical formulas
are unchanged.
See [the English editions README](../README.md) for the exact Chinese source
commit and the incremental-update workflow.

## Build and verification

From the repository root, with Tectonic installed:

```sh
python3 scripts/check_english.py phy
python3 scripts/build_english.py phy --publish
```

The complete build checks source coverage and compiler logs before placing
`Igniting_the_Physics_Spark.pdf` beside this README. It uses the XeTeX engine;
the original XeLaTeX workflow also works from `latex/` using `main.tex`.
The Fandol fonts are supplied by the TeX distribution.

The complete edition passes source coverage (63/63 LaTeX files), structure,
glyph, and reference checks, and compiles with zero overfull-box warnings.
Rendered checks cover the contents, revised headers, affected diagrams, and
the source's closing appendix placeholders. Formula inventories and drawing
paths were compared before and after layout fixes. These checks are not an
independent scientific review of every source claim.

## Source notes

Contributor-approved paragraphs labeled “Translator safety note” appear beside
hazardous source advice, with links to relevant safety guidance. Original prose
remains visible. These annotations are not a comprehensive safety certification;
do not follow an experiment that the adjacent note tells you not to attempt.

The source's chapter 49 stops partway through its discussion, and the book ends
with four unfinished appendix placeholders. Their translation retains that
status rather than inventing the missing material.

This is a translation, not an independent scientific revision. Equations and
plotted diagram geometry are preserved even where the source is inconsistent. For
example, chapter 4's shadow discussion uses a cosine with an inconsistent
angle definition, and chapter 5's final train exercise subtracts the train's
length where it should be added. These are source issues, not new results
established by this edition. The original series discloses AI-generated text;
check important conclusions against standard references.
See [source review notes](SOURCE_NOTES.md) for chapter-specific issues.
