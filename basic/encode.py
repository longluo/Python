#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Encode
# 2015-07-21 04:22:46

# ASCII 
print ord('A')

print chr(65)

# Unicode
print u'中文'

print u'中'

print u'ABC'.encode('utf-8')

print u'中文'.encode('utf-8')

# Format
print '%2d-%02d' % (3, 1)

print '%.2f' % 3.1415926

print 'Age: %s. Gender: %s' % (25, True)



