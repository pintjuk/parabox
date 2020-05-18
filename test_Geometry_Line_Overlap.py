from unittest import TestCase

from Geometry import line


class Testline(TestCase):
    def test_kinda_dont_overlap(self):
        self.assertFalse(line((0, 0), (1, 0)).kindaOverlaps(line((100, 0), (101, 0)), 10, 10))

    def test_kinda_overlaps(self):
        self.assertTrue(line((0, 0), (1, 0)).kindaOverlaps(line((2, 0), (4, 0)), 10, 10))

    def test_kinda_overlaps(self):
        self.assertTrue(line((0, 0), (10, 0)).kindaOverlaps(line((7, 0), (12, 0)), 10, 10))

    def test_kinda_overlaps(self):
        self.assertTrue(line((0, 0), (10, 0)).kindaOverlaps(line((7, 4), (12, 4)), 10, 10))

    def test_kinda_overlaps(self):
        self.assertFalse(line((0, 0), (10, 0)).kindaOverlaps(line((7, 11), (12, 4)), 10, 10))

    def test_kinda_overlaps(self):
        self.assertFalse(line((0, 0), (10, 0)).kindaOverlaps(line((5, 1), (6, 2)), 10, 10, 3))

    def test_kinda_overlaps(self):
        self.assertTrue(line((0, 0), (10, 0)).kindaOverlaps(line((5, 1), (6, 2)), 10, 10, 50))
