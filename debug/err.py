#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Error
# 2015-07-29 15:16:58

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	bar('0')

main()

