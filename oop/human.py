#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OOP Extendsion
# 2015-08-05 02:56:01

class Human(object):
	laugh = 'hahahaha'

	def show_laugh(self):
		print self.laugh

	def laugh_100th(self):
		for i in range(100):
			self.show_laugh()

li_lei = Human()
li_lei.laugh_100th()

def HappyMan(Human):
	def __init__(self, more_words):
		print 'We are happy man.', more_words

han_meimei = HappyMan('Beauty Girl')


		
