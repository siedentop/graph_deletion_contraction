# -*- coding: utf-8 -*-
#!/usr/bin/python3

def fac(n, acc = 1):
    if n == 1:
	return acc
    else:
	return fac(n-1, n * acc)

#def fibonacci(n):
    #''' Return n-1 and n fibonacci numbers.'''
    #i = 1
    #a = 0
    #b = 1
    #while i < n:
	##yield a
	#[a, b] = [b, a+b]
	#i += 1
    #return (a, b)

import numpy as np
def fibonacci(n, mod):
    ''' Returns n-1 and n fibonacci numbers. 
    Fibonacci can be calculated using l * A**n * r.
    '''
    #l = np.array([1, 0])
    A = np.array([[1, 1], [1, 0]])
    r = np.array([[1], [0]])
    As = exponential(A, n-1, mod)
    fib = reduce(np.dot, [As, r])
    #return (As[1][0], fib[0][0])
    return (fib[1][0], fib[0][0])
    
def exponential(A, n, mod):
    ''' From Wikipedia Exponentiation by Squaring
    A is numpy array, n is the power. Returns A**n.'''
    if n < 0:
	raise ValueError('A**n not defined for negative n if A is matrix. (At least not defined here.)')
    elif n==0:
	raise ValueError('Sorry, cant handle n==0')
    elif n==1:
	return np.mod(A, mod)
    elif n % 2 == 0: #n is even
	return exponential(np.mod(reduce(np.dot, [A, A]), mod), n/2, mod)
    else: #n is odd
	return np.mod(reduce(np.dot, [A, exponential(A, n-1, mod)]), mod)

def power(x, n, mod = 1):
    ''' Just like exponential but for scalars '''
    if n <= 0:
	raise ValueError('Nope, dont do that.')
    elif n == 1:
	return x
    elif n % 2 == 0:
	return power(x*x % mod, n/2, mod)
    else:
	return (x * power(x*x % mod, (n-1)/2, mod) ) % mod

def poly(n, x, mod):
    denominator = x**2 + x - 1
    newmod = mod * denominator
    (f1, f2) = fibonacci(n+1, newmod)
    xpower1 = power(x, n+1, newmod)
    numerator = (f1 * xpower1*x + f2 * xpower1 - x ) % newmod
    return numerator / denominator

def calc(n, mod, xmax):
    fib = fibonacci(n + 1, mod)
    print('Fibonacci calculated...')
    s = 0
    for x in range(xmax + 1):
	p = poly(n, x, mod)
	s += p 
	s %= mod
    return s

if __name__=='__main__':
    n = 10**15
    mod = fac(15)
    print(calc(n, mod, 100))
    