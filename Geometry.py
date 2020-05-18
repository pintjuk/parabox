from __future__ import annotations

import math

import numpy as np
from sklearn.decomposition import PCA


def pointsToLineParameters(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    if x1 - x2 == 0:  # avoid devision by zero
        return [90, x1]
    m = (y1 - y2) / (x1 - x2)
    theta = math.atan(m)
    theta = 180 * theta / math.pi
    rho = abs(y1 - (m * x1)) / math.sqrt(m * m + 1)
    return [theta, rho]


class line:
    @classmethod
    def fromTouple(self: line, l):
        return line(l[0], l[1])

    def __init__(self: line, a, b):
        self.a = (a[0], a[1])
        self.b = (b[0], b[1])
        self.lineParameters = pointsToLineParameters(a, b)
        x1 = a[0]
        y1 = a[1]
        x2 = b[0]
        y2 = b[1]
        if x1 - x1 == 0:
            self.m = None
        else:
            self.m = (y1 - y2) / (x1 - x2)
            self.k = y1 - (x1 * self.m)

    def intersection(a: line, b: line):
        x1 = a.a[0]
        y1 = a.a[1]
        x2 = a.b[0]
        y2 = a.b[1]
        x3 = b.a[0]
        y3 = b.a[1]
        x4 = b.b[0]
        y4 = b.b[1]
        denuminator = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        if denuminator == 0:
            return None
        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denuminator
        y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denuminator
        return (x, y)

    def trdistance(a: line, b: line):
        dx = a.lineParameters[0] - b.lineParameters[0]
        dy = a.lineParameters[1] - b.lineParameters[1]
        return math.sqrt(dx * dx + dy * dy)

    def rhodistance(a: line, b: line):
        return abs(a.lineParameters[1] - b.lineParameters[1])

    def thetaDistance(a: line, b: line):
        dr = abs(a.lineParameters[0] - b.lineParameters[0])
        if dr > 90:
            return 180 - dr
        return dr

    def kindaOverlaps(self, line: line, WIDTHS_TRECH, GAP_THRECH, THETA_THRECH=3):
        # Create PCA trasform
        if self.thetaDistance(line) > THETA_THRECH:
            return False
        pca = PCA(n_components=2)
        x = []
        x.append(self.a)
        x.append(self.b)
        x.append(line.a)
        x.append(line.b)
        pca.fit(x)

        # Transform lines into PCA space
        a = pca.transform([self.a, self.b])
        b = pca.transform([line.a, line.b])

        # Check Width of the cluster against width threshold
        pointsInComp2 = [a[0][1], a[1][1], b[0][1], b[1][1], b[0][1], b[1][1], b[0][1], b[1][1]]
        Comp2Width = max([abs(i - ii) for i in pointsInComp2 for ii in pointsInComp2])
        if Comp2Width > WIDTHS_TRECH:
            return False

        # Ceck if they overlap
        if np.sign(a[0][0] - b[0][0]) != np.sign(a[0][0] - b[1][0]):
            return True
        if np.sign(a[1][0] - b[0][0]) != np.sign(a[1][0] - b[1][0]):
            return True

        # Otherwise check if the gap between them is less then the gap threshold
        gap = min([abs(i - b[0][0]) for i in [a[0][0], a[1][0]] for ii in [b[0][0], b[1][0]]])
        return gap < GAP_THRECH


def distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx * dx + dy * dy)
