#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Error Reraise 
# 2015-07-29 15:26:42

def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value: %s' % s)
	return 10 / n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print 'ValueError'
		raise 

bar()

