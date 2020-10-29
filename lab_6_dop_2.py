# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:50:15 2020

@author: admin
"""
from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import solveset

a, b, c, x = symbols('a b c x')
N = CoordSys3D('N')

a = 7 * N.i + 2 * N.j - 8 * N.k
b = -4 * N.i + x * N.j + 9 * N.k

result = a.dot(b) 
result_new = solveset(result, x)

print(result_new)