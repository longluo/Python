#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Set
# 2015年07月21日05:29:45

s = set([1, 2, 3])
print s

# No Same Values
s = set([1, 1, 2, 2, 3, 3])
print s

# Add Key
s.add(5)
print s

# Remove Key
s.remove(2)
print s

# 
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print s1 & s2

print s1 | s2






