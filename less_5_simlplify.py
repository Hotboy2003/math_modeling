# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:32:54 2020

@author: admin
"""
from sympy import symbols
from sympy import sin, cos
from sympy import simplify, expand, factor, trigsimp

x, y, z = symbols('x y z')

simp_expr = simplify(sin(x)**2 + cos(x)**2)
print(simp_expr)

simp_expr = simplify((x**3 + x**2 - x - 1)/(x**2+2*x+1)) #просто все упрощает
print(simp_expr)

simp_expr = expand((x+1)**2) #раскрытие полинома
print(simp_expr)

simp_expr = expand((x + 2) * (x + 3))
print(simp_expr)

simp_expr = expand((x+1)*(x-2) - (x-1)*x)
print(simp_expr)

simp_expr = factor(x**3 - x**2 + x - 1) #все в скобки собирает
print(simp_expr)

simp_expr = expand((cos(x) + sin(x))**2)
print(simp_expr)

simp_expr = factor((cos(x) + sin(x))**2)
print(simp_expr)

simp_expr = trigsimp(sin(x)**2 + cos(x)**2)
print(simp_expr)

simp_expr = trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4)
print(simp_expr)

