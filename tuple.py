#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Tuple
# 2015-07-21 04:56:45

classmates = ('Lisa', 'Sunny', 'Lucy')
print classmates

t = (1, 2)
print t

t = ()
print t

# Only one member
t = (1)
print t

t = (1,)
print t

t = ('a', 'b', ['A', 'B'])
print 'Before: ', t

t[2][0] = 'X'
t[2][1] = 'Y'
print 'After:', t

