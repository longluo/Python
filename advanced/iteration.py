#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Iteration
# 2015-07-21 22:45:20

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print key

for value in d.itervalues():
	print value

for k, v in d.iteritems():
	print k, v

# 字符串迭代
for ch in 'ABCDEFG':
	print ch

# 判断一个对象是可迭代对象
from collections import Iterable
print isinstance('abc', Iterable)

print isinstance([1, 2, 3], Iterable)

print isinstance(123, Iterable)

# 下标循环
for i, value in enumerate(['A', 'B', 'C']):
	print i, value

# 2个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x, y




