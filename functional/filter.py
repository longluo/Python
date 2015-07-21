#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Filter
# 2015-07-22 03:12:38


def is_odd(n):
	return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

def not_empty(s):
	return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])

# Exercise
# Prime Number
def is_prime(n):
	if n == 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

print filter(is_prime, range(1, 101))


