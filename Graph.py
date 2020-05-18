from enum import Enum
from typing import List

import networkx as nx

from Geometry import *

TRANSPARANT_BOX_GRAPH = nx.Graph(
    [(1, 2), (2, 3), (3, 4), (4, 1), (2, 5), (5, 6), (6, 3), (6, 7), (7, 4), (1, 8), (8, 5), (8, 7)])
BOX_GRAPH = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1), (2, 5), (5, 6), (6, 3), (6, 7), (7, 4)])


class Shape(Enum):
    Box = 1
    TransparantBox = 2


class graph:
    def __init__(self, firstLine: line, NODE_TRECH=20):
        self.lines = [(firstLine, [])]
        self.grath = nx.Graph()
        self.NODE_TRECH = NODE_TRECH

    def nodesAreClose(self, a: line, b):
        return min([distance(a.a, b), distance(a.b, b)]) < self.NODE_TRECH

    def plot(self, plt, color='black'):
        for line in self.lines:
            plt.plot(
                [line[0].a[0], line[0].b[0]],
                [line[0].a[1], line[0].b[1]],
                color,
                linewidth=1)
        # for edge in self.grath.edges:
        #     plt.plot(
        #         [edge[0][0], edge[1][0]],
        #         [edge[0][1], edge[1][1]],
        #         color,
        #         linewidth=2)

    def completeEdges(self):
        for line in self.lines:
            if len(line[1]) == 0:
                line[1].append(line[0].a)
                line[1].append(line[0].b)
                self.grath.add_edge(line[1][0], line[1][1])
            if len(line[1]) == 1:
                i = None
                if distance(line[0].a, line[1][0]) < distance(line[0].b, line[1][0]):
                    line[1].append(line[0].b)
                else:
                    line[1].append(line[0].a)
                self.grath.add_edge(line[1][0], line[1][1])

    def tryAdd(self, line: line):
        n1 = None
        n2 = None
        for gline in self.lines:

            def nodeCheck(line_end):
                if self.nodesAreClose(gline[0], line_end):
                    for node in gline[1]:
                        if distance(line_end, node) < self.NODE_TRECH:
                            return node
                    else:
                        i = gline[0].intersection(line)
                        if i == None:  # Lines are parallel, and thus there is no intersection
                            # TODO: Probably something special needs to be done when lines are parallel, Maybe merged?
                            i = line_end
                        self.grath.add_node(i)
                        if len(gline[1]) == 1:
                            self.grath.add_edge(i, gline[1][0])
                        gline[1].append(i)
                        return i

            if n1 == None:
                n1 = nodeCheck(line.a)
            if n2 == None:
                n2 = nodeCheck(line.b)
        if n1 == None and n2 == None:
            return False
        if n1 != None and n2 != None:
            self.grath.add_edge(n1, n2)
        if n1 != None or n2 != None:
            self.lines.append((line, list(filter(lambda x: x != None, [n1, n2]))))
        return True

    def Shape(self):
        if nx.is_isomorphic(self.grath, BOX_GRAPH):
            return Shape.Box
        if nx.is_isomorphic(self.grath, TRANSPARANT_BOX_GRAPH):
            return Shape.TransparantBox
        return None


def construct_graphs(lines: List[line], node_threch=20):
    graphs = []
    lines = list(lines)
    while len(lines) > 0:
        g = graph(lines.pop(), node_threch)
        while True:
            addedlines = []
            for l in lines:
                if g.tryAdd(l):
                    addedlines.append(l)
            if len(addedlines) == 0:
                break
            for l in addedlines:
                lines.remove(l)
        graphs.append(g)

    for g in graphs:
        g.completeEdges()
    print("graph: ", len(graphs))
    for g in graphs:
        print("shape: ", g.Shape())
    return graphs
