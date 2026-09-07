# Igniting the Chemistry and Biology Spark

English translation of the [Chinese chemistry and biology edition](../../chem/README.md),
in three volumes. Translation is in progress; no complete English PDF is
published yet.

The original document class, fonts, geometry, packages, colored boxes, table
definitions, and diagram settings are retained. Prose and printed labels are
translated. See [the English editions README](../README.md) for the Chinese
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
XeLaTeX workflow also works from `latex/`. Fandol fonts come with the TeX
distribution.

During translation, use `--partial` with the checker and `--preview` with the
builder. Preview PDFs are development artifacts outside this directory.
Proofreading and visual review remain necessary even after compiler checks.

## Source and safety notes

The original series discloses AI-generated text. Translation is not scientific
or safety validation. Some source numerical comparisons and explanatory claims
are inconsistent: for example, chapters 5 and 6 contain spelled-out large
numbers that disagree with nearby powers of ten. Formulas and drawing geometry
are retained rather than silently revised.

Chapter 4 also includes a fever-treatment claim involving alcohol rubbing.
That passage is a source claim, not medical guidance from this translation.
Contributor-approved “Translator safety note” paragraphs now warn against this
and other hazardous source advice beside the relevant passages. They cite safety
guidance while leaving the original translated claims visible and styles intact.
The edition's experiments and health-related statements require independent
safety review; do not use this book as a medical or laboratory safety manual.
Read the translated safety front matter before considering any activity.
See [source review notes](SOURCE_NOTES.md) for chapter-specific issues.
