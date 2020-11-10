# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:51:49 2020

@author: student
"""

import tkinter as tk
import random as rd

window = tk.Tk()
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)



label_1 = tk.Label(master=window, text='0')

def brosok():
    value = rd.randint(1,6)
    label_1['text'] = '{}'.format(value)
    
button_1 = tk.Button(text="Бросить",
                     width=25,
                     height=5,
                     bg="blue",
                     fg="yellow",
                     master = window,
                     command = brosok)
    
label_1.grid(row = 1, column = 1, sticky='nsew')
button_1.grid(row=1, column=0)

window.mainloop()