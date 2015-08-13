#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File & Directory
# 2015-08-13 10:49:14

import os

print os.name

print os.uname()

print os.environ

print os.getenv('PATH')

print os.path.abspath('.')

# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
os.path.join('/Users/luolong', 'testdir')
'/Users/luolong/testdir'
# 然后创建一个目录:
os.mkdir('/Users/luolong/testdir')
# 删掉一个目录:
os.rmdir('/Users/luolong/testdir')







