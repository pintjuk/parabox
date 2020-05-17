from __future__ import annotations
from typing import List
from Geometry import *
from sklearn.decomposition import PCA


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
            if cline.thetaDistance(line) < self.ANGLE_THRECH \
                    and cline.rhodistance(line) < self.LINEWIDTH_TRECH:
                self.lines.append(line)
                return True
        return False


def toLines(l):
    return map(lambda x: x.mainLine(), l)


def lineClusters(lines, ANGLE_THRECH=4, LINEWIDTH_TRECH=20):
    cluster: List[Cluster] = []
    if lines is not None:
        for i in range(0, len(lines)):
            l = lines[i][0]
            ltr = line((l[0], l[1]), (l[2], l[3]))
            for c in cluster:
                if c.tryadd(ltr):
                    break
            else:
                cluster.append(Cluster(ltr, ANGLE_THRECH, LINEWIDTH_TRECH))
    print("Num clust: ", len(cluster))
    return cluster
