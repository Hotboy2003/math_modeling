# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import numpy as np
from numpy import cos, sin

window = tk.Tk()

canvas = tk.Canvas()
window.geometry(f'{800}x{800}')
canvas.configure(bg='black')
canvas.pack(fill='both', expand=True) #expand - отображение на экране
label_1 = tk.Entry(master=window, text='введите угол полета')
label_1.place(x = 350, y = 700)
label_2 = tk.Label(master=window, text='введите угол полета')
label_2.place(x = 200, y = 700)
label_3 = tk.Entry(master = window)
label_3.place(x=350, y=730)
label_4 = tk.Label(master=window, text = 'введите скорость ядра')
label_4.place(x = 200, y = 730)

def move_func():
    x0 = 50
    y0 = 650
    
    radius = 10
    
    ball = canvas.create_oval(x0 - radius,
                              y0 - radius,
                              x0 + radius,
                              y0 + radius,
                              fill = 'blue',
                              outline = 'white',
                              width = 4)
    
    return ball

t = np.arange(0,10,0.1)
g = 9.98

def loop_func():
    a = int(label_1.get())
    V = int(label_3.get())
    Vx = V*cos(a)
    Vy = V*sin(a) + g*t
    ball = move_func()
    x = Vx*t
    y = Vy * t + (g * t**2)/2
    
    i = 0
    while True:
        canvas.move(ball, x[i], y[i])
        window.update()
        window.after(100)
        i += 1


    
    
        
btn_create_ball = tk.Button(window,
                                text = 'create ball',
                                command = loop_func)
    
btn_create_ball.place(x = 350, y = 770)
    
window.mainloop()
