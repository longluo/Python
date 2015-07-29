#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Error Raise 
# 2015-07-29 15:22:53

class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

foo('0')


