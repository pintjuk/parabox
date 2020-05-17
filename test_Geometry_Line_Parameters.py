from unittest import TestCase

from Geometry import pointsToLineParameters


class TestLineParameteresOfXAlignedLine(TestCase):
    def test_theta_should_be_0(self):
        self.assertEqual(0, pointsToLineParameters((0,0), (1, 0))[0])

    def test_rho_should_be_0(self):
        self.assertEqual(0, pointsToLineParameters((0,0), (1, 0))[1])


class TestLineParameteresOfXAlignedLineOfset(TestCase):
    def test_theta_should_be_0(self):
        self.assertEqual(0, pointsToLineParameters((0,100), (1, 100))[0])

    def test_rho_should_be_0(self):
        self.assertEqual(100.0, pointsToLineParameters((0,100), (1, 100))[1])


class TestLineParameteresOfdiagonalLine(TestCase):
    def test_theta_should_be_45(self):
        self.assertEqual(45, pointsToLineParameters((0,0), (1, 1))[0])

class TestLineParameteresOfdiagonalLine(TestCase):
    def test_theta_should_be_90(self):
        self.assertEqual(90, pointsToLineParameters((10,0), (10, 1))[0])
    def test_rho_should_be_90(self):
        self.assertEqual(10, pointsToLineParameters((10,0), (10, 1))[1])
