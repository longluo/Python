#!/usr/bin/env python
# -*- coding: utf-8 -*-

# List Comprehensions
# 2015-07-21 23:06:56

# Make a List
print range(1, 11)

# [1x1, 2x2, 3x3, ..., 10x10]
# Method 1
L = []
for x in range(1, 11):
	L.append(x*x)

print L

# Method 2
print [x * x for x in range(1, 11)]


# Add If 
print [x * x for x in range(1, 11) if x % 2  == 0]

# 两层循环，可以生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']


# 列表生成式
import os
print [d for d in os.listdir('.')]

d = {'x': 'A', 'y':'B', 'z':'C'}

for k, v in d.iteritems():
	print k, '=', v

#
L = ['Hello', 'World', 'Apple', 'IBM']
print [s.lower() for s in L]






