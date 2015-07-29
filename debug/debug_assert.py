#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Assert
# 2015-07-29 15:37:00

# print the variable
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero'
	return 10 / n

def main():
	foo('0')

main()

