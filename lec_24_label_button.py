# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:29:34 2020

@author: student
"""

import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(text="zhe4",
                     width=25,
                     height=5,
                     bg="blue",
                     fg="yellow")
button_1.pack()
button_2 = tk.Button(text="moskaley",
                     width=25,
                     height=5,
                     bg="yellow", #фон
                     fg="blue") #цвет текста
button_2.pack() #распаковка кнопки

window.mainloop()