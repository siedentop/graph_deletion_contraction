'''
Created on Sep 22, 2013

@author: chris
'''
import unittest
from main import loops
import networkx as nx


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testLoops(self):
        g = nx.Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 2)
        self.assertEquals(list(loops(g)), [(2,2)])
        g.add_edge(3, 3)
        g.add_edge(3, 2)
        self.assertEqual(list(loops(g)), [(2,2), (3, 3)])

if __name__ == "__main__":
    unittest.main()