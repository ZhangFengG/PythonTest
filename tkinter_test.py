
from tkinter import *
import tkinter.messagebox as messagebox

class Mywidgit(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.pack()
		self.creatWidgit()
	def creatWidgit(self):
		self.label = Label(self,text='this is first')
		self.button = Button(self,text="ok",command=self._helloText)
		self.label.pack()
		self.button.pack()
	def _helloText(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message','hello %s' %name)
a = Mywidgit()
a.master.title("Hello World")
a.mainloop()
