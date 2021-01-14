# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 18:23:00 2021

@author: admin
"""
class Ball:
    
    x_coord = 0
    y_coord = 0
    
    def move_ball(self, vx, vy, t):
        self.x = vx * t + Ball.x_coord #self.x - это локализация переменной 
        self.y = vy * t + Ball.y_coord
        print(f'Переместились в ({self.x}, {self.y})')
        Ball.x_coord += 1
        Ball.y_coord += 1
#все что меняется в классе, менянтся и глобально
ball = Ball() #создание экземпляра класса

ball.move_ball(3, 5, 7)
print(ball.x_coord)

ball_1 = Ball()
print(ball_1.x_coord)
print(ball.x)