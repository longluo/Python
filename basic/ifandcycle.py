#!/usr/bin/env python
# -*- coding: utf-8 -*-

# if else And Cycle
# 2015-07-21 05:08:21


# If
age = 5
if age >= 18:
	print 'your age is', age
	print 'adult'
elif age > 6:
	print 'your age is', age
	print 'teenager'
else:
	print 'kid'


# Cycle
names = ['Jack', 'John', 'Mike']
for name in names:
	print name


# For In
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum


# For 
print 'For Cycle'
sum = 0
for x in range(101):
    sum = sum + x
print sum


# While
print 'While Cycle'
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

