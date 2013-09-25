# -*- coding: utf-8 -*-
# Let R(m,n) be the number of ways to make the m × n grid graph rigid.
# E.g. R(2,3) = 19 and R(5,5) = 23679901
# 
# Define S(N) as ∑R(i,j) for 1 ≤ i, j ≤ N.
# E.g. S(5) = 25021721.
# Find S(100), give your answer modulo 1000000033 

import unittest
from main import RigidGraphs

class TestRigidGraphs(unittest.TestCase):
    def setUp(self):
        self.uut = RigidGraphs()
    def test_rigid(self):
        self.assertEqual(self.uut.rigid(2, 3), 19)
        self.assertEqual(self.uut.rigid(5,5), 23679901)
    def test_rigidSum(self):
        self.assertEqual(self.uut.sum(5), 25021721)

if __name__ == '__main__':
    unittest.main()