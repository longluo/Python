#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Higher Order Function
# 2015-07-22 02:57:11

print abs(-19)

x = abs(-10)
print x

f = abs
print f
print f(-18)

# 传入函数
def add(x, y, f):
	return f(x) + f(y)

print add(-5, 6, abs)

# map/reduce
def f(x):
	return x * x

print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])


# reduce
def add(x, y):
	return x + y

print reduce(add, [1, 3, 5, 7, 9])

def fn(x, y):
	return x * 10 + y

print reduce(fn, [1, 3, 5, 7, 9])



# Exercise

