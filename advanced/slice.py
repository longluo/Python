#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Slice
# 2015-07-21 22:30:10

List = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print [List[0], List[1], List[2]]

# 扩展，取前N个元素
r = []
n = 3
for i in range(n):
	r.append(List[i])

print r

# 切片
print List[0:3]
print List[1:4]

# 倒数切片
print List[-2:]

# 倒数第一个元素的索引是-1
print List[-2:-1]


L = range(100)
print L

# 取前10个数
print L[:10]

# 取后10个数
print L[-10:]

# 取11-20个数
print L[10:20]

# 前10个数，每2个取1个
print L[:10:2]

# 所有数，每5个取1个
print L[::5]

# 复制一个List
print L[:]


# tuple也可以用切片操作
print 'Tuple Slice...'
T = (0, 1, 2, 3, 4, 5)
print T[:3]

# 字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]




