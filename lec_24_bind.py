# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(text = 'najmi',
                     width = 50,
                     height = 50,
                     fg = 'blue')

button_1.pack()

def click_left_mouse(event):
    print('Najalas knopka left')
    
def click_right_mouse(event):
    print('Najalas knopka right')
    
button_1.bind('<Button-1>', click_left_mouse) #покажет какой кнопкой нажали на кнопку
button_1.bind('<Button-3>', click_right_mouse)

window.mainloop()