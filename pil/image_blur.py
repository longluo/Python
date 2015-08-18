#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Image Blur
# 2015-08-19 01:15:08

import Image, ImageFilter

im = Image.open('/Users/luolong/Code/LearnPython/xiaojing2.jpg')

im2 = im.filter(ImageFilter.BLUR)

im2.save('/Users/luolong/Code/LearnPython/pil/blur.jpg', 'jpeg')

