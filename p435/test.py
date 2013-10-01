# -*- coding: utf-8 -*-

import unittest
import numpy as np
from main import *

class TestMainFunctions(unittest.TestCase):

    def test_factorial(self):
	self.assertEqual(fac(3), 6)
	self.assertEqual(fac(5), 120)

    def test_FibSequence(self):
	self.assertEqual((1, 1), fibonacci(2, 100))
	self.assertEqual((1, 2), fibonacci(3, 100))
	self.assertEqual((2, 3), fibonacci(4, 100))
	self.assertEqual((3, 5), fibonacci(5, 100))
	self.assertEqual((5, 8), fibonacci(6, 100))
	self.assertEqual((8, 13), fibonacci(7, 100))
	
    def test_FibSequenceModulus(self):
	for n in range(2, 8):
	    expected = fibonacci(n, 10**15)
	    expected = (expected[0] % 27, expected[1] % 27)
	    self.assertEqual(expected, fibonacci(n, 27))

    def test_FibPoly(self):
	mod = fac(15)
	self.assertEqual(poly(3, 6, mod), 474)
	self.assertEqual(poly(7, 11, mod), 268357683)
    def test_exponential(self):
	A = np.array([[1, 2], [3, 5]])
	n = 5
	As = [A for x in range(n)]
	expected = reduce(np.dot, As)
	np.testing.assert_array_equal(expected, exponential(A, n, 10000))
	
    def test_dataFib(self):
	#fib 10**15 mod 15! is 36651874875
	res = fibonacci(10**15, fac(15))
	print(res[0], res[1])
	self.assertEqual(36651874875, res[0])
    def test_dataFibPoly(self):
	# SUM to 3 for F_3 is 92
	self.assertEqual(calc(3, fac(15), 3), 92)
	# sum to 10 for F10 mod 27 is 14
	self.assertEqual(calc(10, 27, 10), 14)
    def test_FibPolyModulus(self):
	# Values obtained by hand
	self.assertEqual(0, poly(10, 0, 27))
	self.assertEqual(8, poly(10, 1, 27))
	self.assertEqual(24, poly(10, 2, 27))
	self.assertEqual(12, poly(10, 3, 27))
	self.assertEqual(17, poly(10, 4, 27))
	self.assertEqual(24, poly(10, 5, 27))
	self.assertEqual(15, poly(10, 6, 27))
	self.assertEqual(26, poly(10, 7, 27))
	self.assertEqual(6, poly(10, 8, 27))
	self.assertEqual(9, poly(10, 9, 27))
	self.assertEqual(8, poly(10, 10, 27))

    def test_dataFibSeries(self):
	# F_10to15 of 2 mod 15! is 960038235750
	self.assertEqual(960038235750, poly(10**15, 2, fac(15)))

    def test_power(self):
	self.assertEqual(1, power(2, 100, 3))

if __name__ == '__main__':
    unittest.main()
