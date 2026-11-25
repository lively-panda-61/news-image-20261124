"""Entrypoint: stdlib-only copy of entry.png to $MAKEFUN_OUTPUT_DIR.

TDD: written before main.py exists; must fail first.
"""
import hashlib
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(REPO, "main.py")
PNG = os.path.join(REPO, "entry.png")


class TestEntrypoint(unittest.TestCase):
    def test_main_py_is_stdlib_only(self):
        with open(MAIN, encoding="utf-8") as f:
            src = f.read()
        allowed = {"hashlib", "os", "shutil", "sys", "pathlib"}
        for line in src.splitlines():
            s = line.strip()
            if s.startswith("import "):
                for mod in s[7:].split(","):
                    self.assertIn(mod.strip().split(".")[0], allowed, line)
            elif s.startswith("from "):
                self.assertIn(s.split()[1].split(".")[0], allowed, line)

    def test_copy_to_makefun_output_dir(self):
        with tempfile.TemporaryDirectory() as out:
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=out)
            r = subprocess.run(
                [sys.executable, "-P", "-s", MAIN],
                env=env, cwd="/", capture_output=True, text=True,
            )
            self.assertEqual(r.returncode, 0, r.stderr)
            got = os.path.join(out, "entry.png")
            self.assertTrue(os.path.exists(got))
            with open(PNG, "rb") as f:
                want = f.read()
            with open(got, "rb") as f:
                self.assertEqual(f.read(), want)

    def test_default_output_is_slash_output(self):
        with open(MAIN, encoding="utf-8") as f:
            self.assertIn('"/output"', f.read())

    def test_missing_entry_png_fails(self):
        with tempfile.TemporaryDirectory() as d:
            fake_main = os.path.join(d, "main.py")
            with open(MAIN, encoding="utf-8") as f:
                src = f.read()
            with open(fake_main, "w", encoding="utf-8") as f:
                f.write(src)
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=d)
            r = subprocess.run(
                [sys.executable, "-P", "-s", fake_main],
                env=env, cwd=d, capture_output=True, text=True,
            )
            self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
