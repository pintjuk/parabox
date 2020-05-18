from unittest import TestCase

from Geometry import line


class TestIntersectionofTwoLines(TestCase):
    def test_should_intersect_at_a_point_1(self):
        self.assertEqual((1, 1), line((0, 0), (1, 1)).intersection(line((2, 0), (1, 1))))

    def test_should_intersect_at_a_point_1(self):
        self.assertEqual((1, 1), line((0, 0), (0.5, 0.5)).intersection(line((2, 0), (1.5, 0.5))))

    def test_should_intersect_at_a_point_1(self):
        self.assertEqual((1, 1), line((0, 0), (0.5, 0.5)).intersection(line((1, 0), (1, 0.5))))

    def test_parallel_should_not_intersect(self):
        self.assertEqual(None, line((0, 0), (1, 0)).intersection(line((0, 1), (1, 1))))

    def test_non_lines_should_not_intersect_(self):
        self.assertEqual(None, line((0, 0), (0, 0)).intersection(line((0, 1), (1, 1))))
        self.assertEqual(None, line((0, 0), (1, 0)).intersection(line((1, 1), (1, 1))))
