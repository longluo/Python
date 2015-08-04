#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @property
# 2015-07-24 01:41:30

class Student(object):

	def get_score(self):
		print 'score =', self._score
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')

		self._score = value

s = Student()
s.set_score(70)
s.get_score()


class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')

		self._score = value







