# -*- coding: utf-8 -*-

import unittest
import networkx as nx
from main import contract

class TestContract(unittest.TestCase):
    def setUp(self):
        self.g = nx.Graph() # Triangle graph
        self.g.add_edge(1, 2)
        self.g.add_edge(2, 3)
        self.g.add_edge(1, 3)
        
    def test_simple(self):
        newG = contract(self.g, (1,2))
        self.assertEqual(newG.edges(), [(1,3), (1, 3)])
    def test_inputUnmodified(self):
        # Input graph should not be changed.
        _ = contract(self.g, (1,2))
        self.assertEqual(self.g.edges(), [(1, 2), (1,3), (2, 3)])
    def test_MultiGraph(self):
        ''' Doubled edges should become self-loops.'''
        mg = nx.MultiGraph()
        mg.add_edge(1, 2)
        mg.add_edge(1, 2)
        mg.add_edge(2, 3)
        mg.add_edge(1, 3)
        newG = contract(mg, (1, 2))
        self.assertEqual(newG.edges(), [(1, 1), (1, 3), (1, 3)])

if __name__ == '__main__':
    unittest.main()