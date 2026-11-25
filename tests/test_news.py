"""News data integrity: every story must be a verified 24 Nov 2026 story.

TDD: these tests are written before news.py exists and must fail first.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from news import LEADS, BRIEFS, REGIONS, DATE


class TestNewsData(unittest.TestCase):
    def test_date_is_24_nov_2026(self):
        self.assertEqual(DATE, "2026-11-24")

    def test_lead_count(self):
        self.assertEqual(len(LEADS), 6)

    def test_brief_count(self):
        self.assertEqual(len(BRIEFS), 30)

    def test_total_stories(self):
        self.assertEqual(len(LEADS) + len(BRIEFS), 36)

    def test_seven_regions(self):
        regions = {s["region"] for s in LEADS + BRIEFS}
        self.assertEqual(len(regions), 7)
        self.assertEqual(regions, set(REGIONS))

    def test_every_story_dated_24_nov(self):
        for s in LEADS + BRIEFS:
            self.assertEqual(s["date"], "2026-11-24", s["headline"])

    def test_unique_headlines(self):
        heads = [s["headline"] for s in LEADS + BRIEFS]
        self.assertEqual(len(heads), len(set(heads)))

    def test_every_story_has_headline_summary_region(self):
        for s in LEADS + BRIEFS:
            self.assertTrue(s["headline"].strip(), "empty headline")
            self.assertTrue(s["summary"].strip(), "empty summary: " + s["headline"])
            self.assertIn(s["region"], REGIONS)

    def test_headlines_short_enough_to_render(self):
        for s in LEADS:
            self.assertLessEqual(len(s["headline"]), 60, s["headline"])
        for s in BRIEFS:
            self.assertLessEqual(len(s["headline"]), 52, s["headline"])

    def test_no_stale_story(self):
        # The 19 Nov ICJ Myanmar verdict must not appear as a story.
        blob = " ".join(s["headline"] + " " + s["summary"] for s in LEADS + BRIEFS)
        self.assertNotIn("ICJ", blob)
        self.assertNotIn("Myanmar genocide verdict", blob)


if __name__ == "__main__":
    unittest.main()
