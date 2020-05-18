from __future__ import annotations

from typing import List

from sklearn.decomposition import PCA

from Geometry import *


class Cluster:
    def __init__(self: Cluster, first: line, ANGLE_THRECH=4, LINEWIDTH_TRECH=20):
        self.THRESH = 7
        self.lines = [first]
        self.ANGLE_THRECH = ANGLE_THRECH
        self.LINEWIDTH_TRECH = LINEWIDTH_TRECH

    def getPoints(self):
        x = []
        for l in self.lines:
            x.append(l.a)
            x.append(l.b)
        return x

    def mainLine(self):
        x = self.getPoints()
        pca = PCA(n_components=1)
        pca.fit(x)
        xt = pca.transform(x)
        ml = pca.inverse_transform([max(xt), min(xt)])
        return line(ml[0], ml[1])

    def tryadd(self, line: line):
        for cline in self.lines:
            print(cline.rhodistance(line))
            if cline.kindaOverlaps(line, 50, 50, 10):
                self.lines.append(line)
                return True
        return False


def toLines(l):
    return map(lambda x: x.mainLine(), l)


def cvLineTomyLine(lines):
    mylines = []
    if lines is not None:
        for i in range(0, len(lines)):
            l = lines[i][0]
            ltr = line((l[0], l[1]), (l[2], l[3]))
            mylines.append(ltr)
    return mylines


def line_clusters(lines, ANGLE_THRECH=4, LINEWIDTH_TRECH=20):
    cluster: List[Cluster] = []
    lines = cvLineTomyLine(lines)
    while len(lines) > 0:
        c = Cluster(lines.pop(), ANGLE_THRECH, LINEWIDTH_TRECH)
        while True:
            addedLines = []
            for l in lines:
                if c.tryadd(l):
                    addedLines.append(l)
            if len(addedLines) == 0:
                break
            for l in addedLines:
                lines.remove(l)
            cluster.append(c)
    print("Num clust: ", len(cluster))
    return cluster
