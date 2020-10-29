# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:38:10 2020

@author: admin
"""
from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import acos, pi

a, b, c = symbols('a b c')
N = CoordSys3D('N')
a = 0.4 * N.i + 3 * N.j + 0 * N.k
b = -2 *N.i + 8000 * N.j + 7 * N.k
c = -5 * N.i - 6*N.j + 102 * N.k

x1 = a.dot(b) / (a.dot(a)* b.dot(b))
x1 = acos(x1) * 180 / pi
print(x1.evalf())

x2 = a.dot(c) / (a.dot(a)* c.dot(c))
x2 = acos(x2) * 180 / pi
print(x2.evalf())

x3 = b.dot(c) / (c.dot(c)* b.dot(b))
x3 = acos(x3) * 180 / pi
print(x3.evalf())