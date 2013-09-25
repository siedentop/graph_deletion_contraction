# -*- coding: utf-8 -*-
import unittest
import networkx as nx
from main import DeleteContract

class TestDeleteContract(unittest.TestCase):
    def setUp(self):
        self.uut = DeleteContract()
        self.g = nx.Graph() # Triangle graph
        self.g.add_edge(1, 2)
        self.g.add_edge(2, 3)
        self.g.add_edge(1, 3)

    def test_getValue(self):
        self.assertRaises(KeyError, self.uut.getValue, self.g)
        self.uut.addGraph(self.g, 42)
        self.assertEqual(42, self.uut.getValue(self.g))
        # Check same graph but different node names gets valid result
        g = nx.Graph([('a', 'b'), ('b', 'c'), ('a', 'c')])
        self.assertEqual(42, self.uut.getValue(g))
    def test_addGraph(self):
        self.uut.addGraph(self.g, 0)
        self.assertEqual(1, len(self.uut.knownGraphs))
        self.assertEqual([(self.g, 0)], self.uut.knownGraphs[(3,3)])
    def test_getValueEndPoints(self):
        g = nx.Graph()
        g.add_node(1)
        self.assertEqual(1, self.uut.getValue(g))

if __name__ == '__main__':
    unittest.main()