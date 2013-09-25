# -*- coding: utf-8 -*-

import unittest
import networkx as nx
from main import delete

class TestDelete(unittest.TestCase):
    def setUp(self):
        self.g = nx.Graph() # Triangle graph
        self.g.add_edge(1, 2)
        self.g.add_edge(2, 3)
        self.g.add_edge(1, 3)
        
    def test_simple(self):
        newG = delete(self.g, (1,2))
        self.assertEqual(newG.edges(), [(1,3), (2, 3)])
    def test_inputUnmodified(self):
        # Input graph should not be changed.
        _ = delete(self.g, (1,2))
        self.assertEqual(self.g.edges(), [(1, 2), (1,3), (2, 3)])
    def test_MultiGraph(self):
        ''' Doubled edges should only remove one edge. '''
        mg = nx.MultiGraph()
        mg.add_edge(1, 2)
        mg.add_edge(1, 2)
        mg.add_edge(2, 3)
        mg.add_edge(1, 3)
        newG = delete(mg, (1, 2))
        self.assertEqual(newG.edges(), [(1, 2), (1, 3), (2, 3)])

if __name__ == '__main__':
    unittest.main()