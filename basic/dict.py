#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dict 
# 2015-07-21 05:16:31

d = {'Jack':95, 'Tom':99, 'Jerry':56}
print d['Tom']

d['Frank'] = 98
print d

print 'Sunny' in d

print d.get('Sunny', -1)

# Delete a key
d.pop('Tom')

print d


