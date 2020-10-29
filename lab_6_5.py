# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:12:57 2020

@author: admin
"""
from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sqrt

N = CoordSys3D('N')
x, y, z = symbols('x y z')

q1 = 1
q2 = -0.5

E1 = (q1 * x) / sqrt((x**2 + y**2 + z**2)**3) * N.i + (q1*y) / sqrt((x**2 + y**2 + z**2)**3) * N.j + (q1*z) / sqrt((x**2 + y**2 + z**2)**3) * N.k
E2 = (q2 * (x-1)) / sqrt(((x-1)**2 + (y-1)**2 + (z-1)**2)**3) * N.i + (q2 * (y-1)) / sqrt(((x-1)**2 + (y-1)**2 + (z-1)**2)**3) * N.j + (q2 * (z-1)) / sqrt(((x-1)**2 + (y-1)**2 + (z-1)**2)**3)
E_result = E1 + E2
E_result = E_result.subs([(x,3), (y, 4), (z,5)])
E_result_module = E_result.dot(E_result)
print(E_result.evalf())
print(E_result_module.evalf())
