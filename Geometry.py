from __future__ import annotations
import math


def thetarho(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    m = (y1 - y2) / (x1 - x2)
    theta = math.atan(m)
    theta = 180 * theta / math.pi
    rho = abs(y1 - (m * x1)) / math.sqrt(m * m + 1)
    return [theta, rho]


class line:
    def __init__(self: line, a, b):
        self.a = a
        self.b = b
        self.tr = thetarho(a, b)
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
        dx = a.tr[0] - b.tr[0]
        dy = a.tr[1] - b.tr[1]
        return math.sqrt(dx * dx + dy * dy)

    def rhodistance(a: line, b: line):
        return abs(a.tr[1] - b.tr[1])

    def thetaDistance(a: line, b: line):
        dr = abs(a.tr[0] - b.tr[0])
        if dr > 90:
            return 180 - dr
        return dr


def distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx * dx + dy * dy)
