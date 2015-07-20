#!/usr/bin/env python
# -*- coding: utf-8 -*-

# List
# 2015-07-21 04:47:16

classmates = ['Sunny', 'Lisa', 'Frank']

print classmates

print 'length=', len(classmates)

# Append
classmates.append('Adam')
print classmates

# Insert
classmates.insert(1, 'Jack')
print classmates

# pop
classmates.pop()
print classmates

# Cover
classmates[1] = 'Sarah'
print classmates

# Different DataTypes
L = ['Apple', 123456, True]
print L

# List include list
s = ['python', 'java', ['asp', 'php'], 'obj-c']
print 's =', s, ',length=', len(s)

# empty
T = []
print len(T)




