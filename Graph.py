import networkx as nx
from Geometry import *


class graph:
    def __init__(self, firstLine: line, NODE_TRECH=20):
        self.lines = [(firstLine, [])]
        self.grath = nx.Graph()
        self.NODE_TRECH = NODE_TRECH

    def nodesAreClose(self, a: line, b):
        return min([distance(a.a, b), distance(a.b, b)]) < self.NODE_TRECH

    def plot(self, plt, color='black'):
        for edge in self.grath.edges:
            plt.plot(
                [edge[0][0], edge[1][0]],
                [edge[0][1], edge[0][1]],
                color,
                linewidth=2)

    def tryAdd(self, line: line):
        n1 = None
        n2 = None
        for gline in self.lines:
            def nodeCheck(line_end):
                if self.nodesAreClose(gline[0], line.a):
                    for node in gline[1]:
                        if distance(line.a, node) < self.NODE_TRECH:
                            return node
                    else:
                        i = gline[0].intersection(line)
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
        self.lines.append((line, list(filter(lambda x: x != None, [n1, n2]))))
        return True


def ConstructGrahps(clust, node_threch=20):
    graphs = []
    for c in clust:
        l = c.mainLine()
        for g in graphs:
            if g.tryAdd(l):
                break
        else:
            graphs.append(graph(l, node_threch))
    # Clean up graphs
    return graphs
