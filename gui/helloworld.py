#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hello World GUI 
# 2015-08-16 05:58:39

'First GUI Program'

from Tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello, World')
		self.helloLabel.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()

app = Application()

app.master.title('Hello World')

app.mainloop()

		