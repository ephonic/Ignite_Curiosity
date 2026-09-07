#!/usr/bin/env python3
"""Build English editions in isolated directories and check their logs.

Normal builds require complete translations. --preview explicitly permits
missing chapters and never publishes PDFs into EN/. --publish copies verified
complete PDFs beside each subject README, matching the Chinese layout.
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from check_english import ROOT, BOOKS, check_book


ENTRIES = {
    "math": [("main.tex", "Igniting_the_Mathematical_Spark.pdf")],
    "phy": [("main.tex", "Igniting_the_Physics_Spark.pdf")],
    "chem": [
        ("book.tex", "Igniting_the_Chemistry_and_Biology_Spark.pdf"),
        ("vol1.tex", None), ("vol2.tex", None), ("vol3.tex", None),
    ],
    "literal_arts": [("literal_book.tex", "Igniting_the_Liberal_Arts_Spark.pdf")],
}
INPUT = re.compile(r"\\(?:input|include)\{([^{}]+)\}")
BAD_LOG = re.compile(
    r"^.*(?:No file .*\.tex|Missing character:|Undefined control sequence|"
    r"LaTeX Error:|(?:Reference|Citation) .* undefined|"
    r"There were undefined references).*$", re.MULTILINE
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("books", nargs="*", help="Subjects to compile (default: all)")
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    selected = args.books or BOOKS
    if any(book not in BOOKS for book in selected):
        parser.error("Unknown subject")
    if args.preview and args.publish:
        parser.error("A partial preview cannot be published as a complete book")
    engine = shutil.which("tectonic")
    if not engine:
        parser.error("Tectonic is required for this build script; sources also support XeLaTeX")
    output = args.output_dir or Path(tempfile.mkdtemp(prefix="ignite-english-build-"))
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    print(f"Build directory: {output}", flush=True)
    if args.preview:
        print("PARTIAL PREVIEW: missing chapters will be listed and omitted.", flush=True)
    publications = []
    for book in selected:
        source_dir = ROOT / "EN" / book / "latex"
        if not source_dir.is_dir():
            raise SystemExit(f"Missing English directory: {source_dir}")
        if book == "literal_arts" and not args.preview:
            subprocess.run([sys.executable, str(ROOT / "scripts/assemble_liberal_arts.py")], check=True)
        elif book == "literal_arts":
            subprocess.run([sys.executable, str(ROOT / "scripts/assemble_liberal_arts.py"), "--check"], check=True)
        if book != "literal_arts" or not args.preview:
            if not check_book(book, partial=args.preview):
                raise SystemExit(f"Source validation failed: {book}")
        staging = output / book / "source"
        staging.mkdir(parents=True, exist_ok=True)
        for source in source_dir.rglob("*.tex"):
            target = staging / source.relative_to(source_dir)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        if book == "literal_arts" and args.preview:
            from assemble_liberal_arts import source_fragments
            fragments = []
            for name, _ in source_fragments():
                fragment = source_dir / "fragments" / name
                if fragment.is_file():
                    fragments.append(fragment.read_text(encoding="utf-8").rstrip("\n") + "\n")
                else:
                    print(f"PREVIEW omits {book}/{name}", flush=True)
            text = "".join(fragments)
            if "\\begin{document}" not in text or "\\end{document}" not in text:
                raise SystemExit("Preview requires translated preamble and final fragment")
            (staging / "literal_book.tex").write_text(text, encoding="utf-8")
        if args.preview:
            # Modify only staging copies; never create source placeholders.
            for path in staging.rglob("*.tex"):
                def omit_missing(match):
                    relative = Path(match.group(1))
                    if not relative.suffix:
                        relative = relative.with_suffix(".tex")
                    if (staging / relative).is_file():
                        return match.group(0)
                    print(f"PREVIEW omits {book}/{relative}", flush=True)
                    return ""
                path.write_text(INPUT.sub(omit_missing, path.read_text(encoding="utf-8")), encoding="utf-8")
        for entry, publication_name in ENTRIES[book]:
            destination = output / book / Path(entry).stem
            destination.mkdir(parents=True, exist_ok=True)
            transcript = destination / "build.txt"
            with transcript.open("w", encoding="utf-8") as stream:
                result = subprocess.run(
                    [engine, "--keep-logs", "--outdir", str(destination), entry],
                    cwd=staging, stdout=stream, stderr=subprocess.STDOUT, check=False,
                )
            log_path = destination / Path(entry).with_suffix(".log")
            log = log_path.read_text(encoding="utf-8", errors="replace") if log_path.exists() else ""
            failures = BAD_LOG.findall(log)
            if result.returncode or failures or not log_path.exists():
                print(f"FAILED: {book}/{entry}; see {transcript}", flush=True)
                for failure in failures[:30]:
                    print(failure)
                raise SystemExit(1)
            pdf = destination / Path(entry).with_suffix(".pdf")
            if not pdf.is_file():
                raise SystemExit(f"Compiler did not produce {pdf}")
            overfull = len(re.findall(r"Overfull \\[hv]box", log))
            print(f"BUILT {pdf} ({overfull} overflow warnings; visual review required)", flush=True)
            if args.publish and publication_name:
                target = ROOT / "EN" / book / publication_name
                publications.append((pdf, target))
    # Do not replace any edition PDF until all requested entrypoints pass.
    for pdf, target in publications:
        shutil.copy2(pdf, target)
        print(f"Published complete PDF: {target}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
