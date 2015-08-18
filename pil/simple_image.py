#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Simple image process by PIL
# 2015-08-19 01:00:46

import Image

# open a jpg file
img = Image.open('/Users/luolong/Code/LearnPython/xiaojing2.jpg')

# get image file size
w, h = img.size

# to 50% 
img.thumbnail((w//2, h//2))

# save as jpeg
img.save('/Users/luolong/Code/LearnPython/pil/thumbnail.jpeg')


