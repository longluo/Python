#!/usr/bin/env python
# -*- coding: utf-8 -*-

# JSON
# 2015-08-13 11:02:26

#JSON类型	Python类型
# {}	dict
# []	list
# "string"	'str'或u'unicode'
# 1234.56	int或float
# true/false	True/False
# null	None

import json

d = dict(name='Frank', age=27, score=96)
print json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

	def student2dict(std):
		return {
			'name': std.name,
			'age': std.age,
			'score': std.score
		}

	def dict2student(d):
		return Student(d['name'], d['age'], d['score'])


s = Student('Frank', 26, 95)
#print(json.dumps(s))

print(json.dumps(s, default=student2dict))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))






