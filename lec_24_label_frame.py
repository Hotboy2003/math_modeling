# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:35:11 2020

@author: student
"""

  
import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame() #компановвщик (подокно)
frame_b = tk.Frame()

label_a = tk.Label(master=frame_b, text="haha")
label_a.pack()
label_b = tk.Label(master=frame_a, text="im so sad ;(")
label_b.pack()


frame_a.pack()
frame_b.pack()
window.mainloop()