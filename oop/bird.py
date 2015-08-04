#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bird 
# 2015-08-05 02:46:25

# 
class Bird(object):
	# attribute
	have_feather = True
	way_of_reproduction = 'egg'

	# method
	def move(self, dx, dy):
		position = [0, 0]
		position[0] = position[0] + dx
		position[1] = position[1] + dy
		return position

penguin = Bird()
print 'after move:', penguin.move(5, 8)

# inheritance
class Chicken(Bird):
	 way_of_move = 'walk'
	 possible_in_KFC = True


class Oriole(Bird):
	way_of_move = 'fly'
	possible_in_KFC = False

summer = Chicken()

print summer.have_feather
print summer.move(5, 8)


		
		
