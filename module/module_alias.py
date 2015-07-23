#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Module Alias
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





