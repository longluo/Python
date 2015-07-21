#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Function Iteration
# 2015-07-21 14:54:07

def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

print fact(1), fact(5), fact(100)


# 通过尾递归优化
def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

print fact(10)


