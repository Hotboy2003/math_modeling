# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:36:06 2020

@author: student
"""

import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=10)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(master=window,
                         relief=tk.RAISED, #делает кнопки объемными
                         borderwidth=1)
        frame.grid(row=i, column=j) #создает сетку, роу - строчка, колумн - столбец
        button = tk.Button(master=frame,
                         text=f"мать {i} \n отец{j}")
        button.pack()

window.mainloop()