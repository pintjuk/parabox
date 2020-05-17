from __future__ import annotations
import math


def pointsToLineParameters(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    if x1-x2 == 0: # avoid devision by zero
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
        self.m = (y1 - y2) / (x1 - x2)
        self.k = y1 - (x1 * self.m)

    def intersection(a: line, b: line):
        x = (b.k - a.k) / (a.m - b.m)
        y = x * b.m + b.k
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


def distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx * dx + dy * dy)
