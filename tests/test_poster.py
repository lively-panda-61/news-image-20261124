"""Poster file: 1024x1024 PNG, at most 1 MiB, whole image.

TDD: written before entry.png exists; must fail first.
"""
import os
import struct
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(REPO, "entry.png")


class TestPoster(unittest.TestCase):
    def test_png_exists(self):
        self.assertTrue(os.path.exists(PNG))

    def test_png_signature(self):
        with open(PNG, "rb") as f:
            self.assertEqual(f.read(8), b"\x89PNG\r\n\x1a\n")

    def test_size_1024x1024(self):
        with open(PNG, "rb") as f:
            f.seek(16)
            w, h = struct.unpack(">II", f.read(8))
        self.assertEqual((w, h), (1024, 1024))

    def test_at_most_1mib(self):
        self.assertLessEqual(os.path.getsize(PNG), 1048576)

    def test_not_blank(self):
        # A real poster is far larger than an empty canvas would compress to.
        self.assertGreater(os.path.getsize(PNG), 100000)


if __name__ == "__main__":
    unittest.main()
