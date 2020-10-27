# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:57:42 2020

@author: admin
"""
from sympy import symbols
from sympy import sin, cos
from sympy import simplify, expand, factor, trigsimp, sqrt
x = symbols('x')

simp_expr = simplify((sqrt(x) - x/(sqrt(x) + 1)) * (x-1)/sqrt(x))
print(simp_expr)