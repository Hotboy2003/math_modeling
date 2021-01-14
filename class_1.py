# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:58:00 2021

@author: admin
"""
class Ball: #всегда с большой буквы название класса

    #создадим атрибуты класса
    color = 'red'
    radius = 5
    #функция внутри класса - это метод
    def update_parameters(self): #всегда пишем self - означает, что этот метод будет использован экземпляром класса
        print('Изменили цвет')
        
    def move_ball(self, vx0=0):
        print(f'Мячик приобрел скорость {vx0}')
        
# создадим экзепляр класса

ball_1 = Ball()
ball_2 = Ball()

print(type(ball_1))
print(type(2))

ball_1.move_ball() #выполняет функцию move_ball
print(ball_2.color)

print(dir(ball_1))