#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Function
# 2015-07-21 05:49:55

import math


def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print my_abs(5), my_abs(-15)


def nop():
	pass

# Second Edition
def my_abs_v2(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print my_abs_v2(25)


# Return serval Values
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y

ret = move(100, 100, 60, math.pi / 6)
print 'ret = ', ret




