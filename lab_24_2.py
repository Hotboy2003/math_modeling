# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:12:10 2020

@author: student
"""

import tkinter as tk
window = tk.Tk()

label_1 = tk.Entry(master=window, text='введите число и укажите единицу измерения')
label_1.pack()
label_2 = tk.Label()
label_3 = tk.Label()



def c():
    label_3['text'] = 'Цельсии'
    
def k():
    label_3['text'] = 'Кельвины'
    
def C():
    value= label_1.get()
    x = label_3['text']
    if x == 'Цельсии':
        label_2['text'] = '{}'.format(int(value))
    elif x == 'Кельвины':
        label_2['text'] = '{}'.format(int(value) - 273.15)
  
def K():
    value= label_1.get()
    x = label_3['text']
    if x == 'Цельсии':
        label_2['text'] = '{}'.format(int(value) + 273.15)
    elif x == 'Кельвины':
        label_2['text'] = '{}'.format(int(value))
    
button_3 = tk.Button(text='конвертировать в Цельсии', command=C)
button_4 = tk.Button(text='конвертировать в Кельвины', command=K)
button_1 = tk.Button(text='C', command=c)
button_2 = tk.Button(text='K', command=k)
button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()
label_2.pack()
label_3.pack()

window.mainloop()