# Igniting the Physics Spark

English translation of the [Chinese physics edition](../../phy/README.md).
Translation is in progress; no complete English PDF is published yet.

The original document class, fonts, geometry, packages, colored boxes, and
diagram settings are retained. Prose and visible labels are translated.
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

While translation is incomplete, `--partial` on the checker and `--preview`
on the build script permit development checks. Preview PDFs stay outside the
edition directory and must not be mistaken for a complete translation.
Compiler success does not replace proofreading and visual review.

## Source notes

The source ends with four unfinished appendix placeholders. Their translation
retains that status rather than inventing the missing material.

This is a translation, not an independent scientific revision. Equations and
diagram geometry are preserved even where the source is inconsistent. For
example, chapter 4's shadow discussion uses a cosine with an inconsistent
angle definition, and chapter 5's final train exercise subtracts the train's
length where it should be added. These are source issues, not new results
established by this edition. The original series discloses AI-generated text;
check important conclusions against standard references.
