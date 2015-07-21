#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generator
# 2015-07-22 00:50:04

L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
print g

print g.next()


g = (x * x for x in range(10))
for n in g:
	print n

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print b
		a, b = b, a + b
		n = n + 1

print fib(6)

# Yield
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1

print fib(6)


def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 3
	print 'step 3'
	yield 5

o = odd()
print o.next()


