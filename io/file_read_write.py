#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Read & Write
# 2015-07-25 00:43:49

# File Not Exist
#f = open('/Users/luolong/test.txt', 'r')
#print f

# File Exist
f = open('/Users/luolong/Code/LearnPython/jingyan.txt', 'r')

print f.read()

f.close()

# Make f always close
try:
	f = open('/Users/luolong/Code/LearnPython/jingyan.txt', 'r')
	print f.read()
finally:
	if f:
		f.close()

# use with
with open('/Users/luolong/Code/LearnPython/jingyan.txt', 'r') as f:
	print f.read()

# huge size file
f = open('/Users/luolong/Code/LearnPython/jingyan.txt', 'r')
print f.read(10)

for line in f.readlines():
	print(line.strip())


# file-like object
# open a image file.
f = open('/Users/luolong/Code/LearnPython/xiaojing2.jpg', 'rb')
print f.read()


# write a file.
f = open('/Users/luolong/Code/LearnPython/test.txt', 'w')
f.write('Hello Python')
f.close()

# use with 
with open('/Users/luolong/Code/LearnPython/test.txt', 'w') as f:
	f.write('Hello, Python')















