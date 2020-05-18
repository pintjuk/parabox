from unittest import TestCase

import networkx as nx

from Geometry import line
from Graph import construct_graphs


class TestNoLines(TestCase):
    def test_should_construct_nothing(self):
        graphs = construct_graphs([])
        self.assertEqual(0, len(graphs), "should be one graph")


class TestOneLine(TestCase):
    def setUp(self) -> None:
        # Arange
        lines = map(lambda x: line.fromTouple(x), [((0, 0), (100, 100))])
        # Act
        self.graphs = construct_graphs(lines)

    def test_should_be_one_graph(self):
        self.assertEqual(1, len(self.graphs), "should be one graph")

    def test_should_have_1_line(self):
        self.assertEqual(1, len(self.graphs[0].lines), "should have 1 line")

    def test_should_have_2_nodes(self):
        self.assertEqual(2, len(self.graphs[0].grath.nodes), "should have 2 nodes")

    def test_should_have_1_edge(self):
        self.assertEqual(1, len(self.graphs[0].grath.edges), "should have 1 edge")

    def test_should_have_right_valancy(self):
        self.assertEqual(1, self.graphs[0].grath.degree((0, 0)), "valency should be 1")
        self.assertEqual(1, self.graphs[0].grath.degree((100, 100)), "valency should be 1")


class TestConstructTwoConnectedLine(TestCase):
    def setUp(self) -> None:
        # Arange
        lines = map(lambda x: line.fromTouple(x), [((0, 0), (100, 100)), ((0, 0), (-100, 100))])
        # Act
        self.graphs = construct_graphs(lines)

    def test_should_be_one_graph(self):
        self.assertEqual(1, len(self.graphs))

    def test_should_have_2_line(self):
        self.assertEqual(2, len(self.graphs[0].lines))

    def test_should_have_3_nodes(self):
        self.assertEqual(3, len(self.graphs[0].grath.nodes))

    def test_should_have_2_edge(self):
        self.assertEqual(2, len(self.graphs[0].grath.edges))

    def test_should_have_right_valancy(self):
        self.assertEqual(2, self.graphs[0].grath.degree((0, 0)))
        self.assertEqual(1, self.graphs[0].grath.degree((100, 100)))
        self.assertEqual(1, self.graphs[0].grath.degree((-100, 100)))


class TestConstructThreeConnectedLine(TestCase):
    def setUp(self) -> None:
        # Arange
        l = [((0, 0), (100, 100)),
             ((0, 0), (-100, 100)),
             ((0, 0), (-100, -100)),
             ]
        # Act
        self.graphs = construct_graphs(map(lambda x: line.fromTouple(x), l))

    def test_should_be_one_graph(self):
        self.assertEqual(1, len(self.graphs))

    def test_should_have_3_line(self):
        self.assertEqual(3, len(self.graphs[0].lines))

    def test_should_be_isomorphic_to_a_cross(self):
        self.assertTrue(nx.is_isomorphic(self.graphs[0].grath, nx.Graph([(1, 2), (1, 3), (1, 4)])))


class TestConstructFourConnectedLine(TestCase):
    def setUp(self) -> None:
        # Arange
        l = [((0, 0), (100, 100)),
             ((0, 0), (-100, 100)),
             ((0, 0), (-100, -100)),
             ((0, 0), (100, -100)),
             ]
        # Act
        self.graphs = construct_graphs(map(lambda x: line.fromTouple(x), l))

    def test_should_be_one_graph(self):
        self.assertEqual(1, len(self.graphs))

    def test_should_have_4_line(self):
        self.assertEqual(4, len(self.graphs[0].lines))

    def test_should_be_isomorphic_to_a_star(self):
        self.assertTrue(nx.is_isomorphic(self.graphs[0].grath, nx.Graph([(1, 2), (1, 3), (1, 4), (1, 5)])))


class TestConstructTriangle(TestCase):
    def setUp(self) -> None:
        # Arange
        l = [((0, 0), (100, 100)),
             ((0, 0), (-100, 100)),
             ((100, 100), (-100, 100)),
             ]
        # Act
        self.graphs = construct_graphs(map(lambda x: line.fromTouple(x), l))

    def test_should_be_one_graph(self):
        self.assertEqual(1, len(self.graphs))

    def test_should_have_3_line(self):
        self.assertEqual(3, len(self.graphs[0].lines))

    def test_should_be_isomorphic_to_a_triangle(self):
        self.assertTrue(nx.is_isomorphic(self.graphs[0].grath, nx.Graph([(1, 2), (1, 3), (2, 3)])))


class TestConstructSquar(TestCase):
    def setUp(self) -> None:
        # Arange
        l = [((1, 1), (1, 100)),
             ((1, 100), (100, 100)),
             ((100, 100), (100, 1)),
             ((100, 1), (1, 1)),
             ]
        # Act
        self.graphs = construct_graphs(map(lambda x: line.fromTouple(x), l))

    def test_should_be_one_graph(self):
        self.assertEqual(1, len(self.graphs))

    def test_should_have_4_line(self):
        self.assertEqual(4, len(self.graphs[0].lines))

    def test_should_be_isomorphic_to_a_triangle(self):
        self.assertTrue(nx.is_isomorphic(self.graphs[0].grath, nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1)])))


class TestConstructChair(TestCase):
    def setUp(self) -> None:
        # Arange
        l = [((5, 3), (1, 100)),
             ((1, 100), (100, 100)),
             ((100, 100), (100, 1)),
             ((100, 1), (-1, -1)),
             ((100, -1), (201, 1)),
             ((200, 0), (203, 100)),
             ((200, 100), (100, 100)),
             ]
        # Act
        self.graphs = construct_graphs(map(lambda x: line.fromTouple(x), l))

    def test_should_be_one_graph(self):
        self.assertEqual(1, len(self.graphs))

    def test_should_have_7_line(self):
        self.assertEqual(7, len(self.graphs[0].lines))

    def test_should_be_isomorphic_to_a_triangle(self):
        self.assertTrue(
            nx.is_isomorphic(self.graphs[0].grath, nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1), (2, 5), (5, 6), (6, 3)])))


class TestConstructNontransparantCube(TestCase):
    def setUp(self) -> None:
        # Arange
        l = [((0, 0), (1, 110)),
             ((1, 100), (100, 100)),
             ((100, 100), (100, 1)),
             ((100, 1), (1, 1)),
             ((100, 1), (200, 1)),
             ((200, 1), (200, 100)),
             ((200, 100), (100, 100)),
             ((1, 100), (100, 200)),
             ((200, 100), (100, 200)),
             ]
        # Act
        self.graphs = construct_graphs(map(lambda x: line.fromTouple(x), l))

    def test_should_be_one_graph(self):
        self.assertEqual(1, len(self.graphs))

    def test_should_have_9_line(self):
        self.assertEqual(9, len(self.graphs[0].lines))

    def test_should_be_isomorphic_to_a_triangle(self):
        self.assertTrue(nx.is_isomorphic(self.graphs[0].grath, nx.Graph(
            [(1, 2), (2, 3), (3, 4), (4, 1), (2, 5), (5, 6), (6, 3), (6, 7), (7, 4)])))


class TestConstructNontransparantCube(TestCase):
    def setUp(self) -> None:
        # Arange
        l = [((0, 0), (1, 110)),
             ((1, 100), (100, 100)),
             ((100, 100), (100, 1)),
             ((100, 1), (1, 1)),
             ((100, 1), (200, 1)),
             ((200, 1), (200, 100)),
             ((200, 100), (100, 100)),
             ((1, 100), (100, 200)),
             ((200, 100), (100, 200)),
             ((1, 1), (100, -200)),
             ((200, 1), (100, -200)),
             ((100, -200), (100, 200))
             ]
        # Act
        self.graphs = construct_graphs(map(lambda x: line.fromTouple(x), l))

    def test_should_be_one_graph(self):
        self.assertEqual(1, len(self.graphs))

    def test_should_have_12_line(self):
        self.assertEqual(12, len(self.graphs[0].lines))

    def test_should_be_isomorphic_to_a_triangle(self):
        self.assertTrue(nx.is_isomorphic(self.graphs[0].grath, nx.Graph(
            [(1, 2), (2, 3), (3, 4), (4, 1), (2, 5), (5, 6), (6, 3), (6, 7), (7, 4), (1, 8), (8, 5), (8, 7)])))
