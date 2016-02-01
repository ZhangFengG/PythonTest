#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox


class MyAPP(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creatWidget()

    def creat_widget(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.button = Button(self, text='ok', command=self._hello)
        self.button.pack()

    def _hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('message', 'hello , %s' % name)
app = MyAPP()

app.master.title('H')

app.mainloop()