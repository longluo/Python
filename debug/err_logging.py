#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Error Logging
# 2015-07-29 15:18:48

import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)

main()
print 'END'

