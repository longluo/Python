#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Error Process
# 2015-07-29 14:50:43

# def foo():
# 	r = some_function()
# 	if r == (-1):
# 		return (-1)

# 	# do something
# 	return r


# def bar():
# 	r = foo()
# 	if r == (-1):
# 		print ('Error')
# 	else:
# 		pass


def foo():
	pass


# try
try:
	print 'try...'
	r = 10 / 0
	print 'result:', r
except ZeroDivisionError as e:
	print 'except:', e
finally:
	print 'finally...'
print 'END'


# Correct
print 'Correct'
try:
	print 'try...'
	r = 10 / 5
	print 'result:', r
except ZeroDivisionError as e:
	print 'except:', e
finally:
	print 'finally...'
print 'END'

# Different Error Types
print 'Different Error Types'
try:
	print 'try...'
	r = 10 / int('a')
	print 'result:', r
except ValueError as e:
	print 'ValueError:', e
except ZeroDivisionError as e:
	print 'ZeroDivisionError:', e
finally:
	print 'finally...'
print 'END'

# No Error
print 'No Error'
try:
	print 'try...'
	r = 10 / int('2')
	print 'result:', r
except ValueError as e:
	print 'ValueError:', e
except ZeroDivisionError as e:
	print 'ZeroDivisionError:', e
else:
	print 'no error!'
finally:
	print 'finally...'
print 'END'


# All error extends from BaseException
try:
	foo()
except ValueError as e:
	print 'ValueError'
except UnicodeError as e:
	print 'UnicodeError'

# 跨越多层调用
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		print 'Error:', e
	finally:
		print 'finally...'


# 调用堆栈

