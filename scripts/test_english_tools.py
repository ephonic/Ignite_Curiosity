#!/usr/bin/env python3
"""Regression tests for English-edition validation and publication safeguards."""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_english
import check_english
from assemble_liberal_arts import source_fragments, SOURCE


class StructureTests(unittest.TestCase):
    def test_only_explicit_source_glyph_examples_are_allowed(self):
        allowed = check_english.HAN_EXAMPLES["ch014.tex"]
        check = check_english.has_untranslated_han
        self.assertFalse(check(r"The character \mbox{妈} means mother.", "妈", allowed))
        self.assertTrue(check("Unmarked 妈", "妈", allowed))
        self.assertTrue(check(r"\mbox{未翻译}", "未翻译", allowed))
        self.assertTrue(check(r"\mbox{妈}", "not present in source", allowed))
        self.assertTrue(check(r"\mbox{妈}", "妈"))

    def test_fragments_reconstruct_source(self):
        fragments = source_fragments()
        self.assertEqual("".join(text for _, text in fragments), SOURCE.read_text(encoding="utf-8"))
        self.assertEqual(sum(name.startswith("ch") for name, _ in fragments), 114)

    def test_only_exact_pagination_block_is_allowed(self):
        for name, content in check_english.PAGINATION_BLOCKS.items():
            with self.subTest(name=name):
                block = f"% EN-PAGINATION-BEGIN {name}\n{content}% EN-PAGINATION-END {name}\n"
                self.assertEqual(check_english.normalize_pagination(block), "")
                with self.assertRaises(ValueError):
                    check_english.normalize_pagination(block.replace("\\toprule", "\\hline"))
        name = "thinking-tools"
        content = check_english.PAGINATION_BLOCKS[name]
        block = f"% EN-PAGINATION-BEGIN {name}\n{content}% EN-PAGINATION-END {name}\n"
        self.assertEqual(check_english.normalize_pagination("before\n" + block + "after"), "before\nafter")
        with self.assertRaises(ValueError):
            check_english.normalize_pagination(block.replace("llX", "XXX"))
        with self.assertRaises(ValueError):
            check_english.normalize_pagination(block.replace("thinking-tools", "unknown"))
        with self.assertRaises(ValueError):
            check_english.normalize_pagination(block.replace("EN-PAGINATION-END", "BROKEN-END"))

    def test_missing_sources_are_fatal_except_in_partial_mode(self):
        with tempfile.TemporaryDirectory(prefix="english-check-test-") as directory:
            root = Path(directory)
            source = root / "math/latex"
            source.mkdir(parents=True)
            (source / "main.tex").write_text("\\chapter{Example}\n", encoding="utf-8")
            with patch.object(check_english, "ROOT", root), contextlib.redirect_stdout(io.StringIO()):
                self.assertFalse(check_english.check_book("math", partial=False))
                self.assertTrue(check_english.check_book("math", partial=True))

    def test_style_and_structure_changes_are_detected(self):
        original = "\\documentclass{book}\n\\usepackage{xcolor}\n\\chapter{Example}\n\\label{one}\n"
        with tempfile.TemporaryDirectory(prefix="english-style-test-") as directory:
            root = Path(directory)
            source = root / "math/latex/main.tex"
            target = root / "EN/math/latex/main.tex"
            source.parent.mkdir(parents=True)
            target.parent.mkdir(parents=True)
            source.write_text(original, encoding="utf-8")
            with patch.object(check_english, "ROOT", root), contextlib.redirect_stdout(io.StringIO()):
                target.write_text(original, encoding="utf-8")
                self.assertTrue(check_english.check_book("math", partial=False))
                for changed in (
                    original.replace("{book}", "{article}"),
                    original.replace("{xcolor}", "{color}"),
                    original.replace("\\chapter", "\\section"),
                    original.replace("{one}", "{two}"),
                    original.replace("Example", "未翻译"),
                ):
                    target.write_text(changed, encoding="utf-8")
                    self.assertFalse(check_english.check_book("math", partial=False))


class BuildTests(unittest.TestCase):
    def test_preview_cannot_publish(self):
        with patch("sys.argv", ["build_english.py", "--preview", "--publish"]):
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
                build_english.main()
        self.assertEqual(caught.exception.code, 2)

    def test_bad_log_messages_are_rejected(self):
        for line in (
            "No file chapters/ch05.tex.",
            "Missing character: There is no glyph",
            "! Undefined control sequence.",
            "! LaTeX Error: File missing.",
            "LaTeX Warning: Reference `one' on page 3 undefined",
            "LaTeX Warning: There were undefined references.",
        ):
            self.assertTrue(build_english.BAD_LOG.search(line), line)
        self.assertFalse(build_english.BAD_LOG.search("No file main.toc."))


if __name__ == "__main__":
    unittest.main()
