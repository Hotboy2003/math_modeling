# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:12:05 2020

@author: admin
"""
from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sin, cos, trigsimp

N = CoordSys3D('N')
a, b, c = symbols('a b c')

v = N.i - 2*N.j
print(v/3)
print(v*4/3)

v1 = 2*N.i + 3*N.j - N.k
v2 = N.i - 4*N.j + N.k
sol = v1.dot(v2) #скалярное произведение
print(sol)

#cross - векторное произведение

v = (a*b + a*c + b**2 + b*c)*N.i + N.j
sol = v.factor() #украшает вектор
print(sol)

v = (sin(a)**2 + cos(a)**2)*N.i - (2*cos(b)**2-1)*N.k
sol = trigsimp(v)
print(sol)