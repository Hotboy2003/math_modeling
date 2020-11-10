# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:32:47 2020

@author: student
"""

import tkinter as tk

window = tk.Tk()

entry_1 = tk.Entry(fg="yellow",
                   bg="black",
                   width=50)

name = entry_1.get()
entry_1.insert(0, "123 ") #вставляет текст
entry_1.delete(0, 1) #убирает одну единицу текста с начала
entry_1.pack()

window.mainloop()