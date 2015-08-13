#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pickling
# 2015-08-13 10:59:09

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

try:
	import cPickle as pickle
except ImportError:
	import pickle

d = dict(name='Frank', age=27, score=96)
print pickle.dumps(d)





