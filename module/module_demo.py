#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Module Demo
# include Alias and Action Scope
# 2015-07-24 00:58:32

# cStringIO
try:
	import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
	import StringIO

# simpleJSON
try:
	import json
except ImportError:
	import simplejson as json


# Action Scope
def _private_1(name):
	return 'Hello, %s' % name

def _private_2(name):
	return 'Hi, %s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)





