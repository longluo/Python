#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Return 
# 2015年07月22日03:37:59

def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1, 3, 5, 7, 9)
print f
print f()



