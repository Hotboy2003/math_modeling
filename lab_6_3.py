# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:02:39 2020

@author: admin
"""
from sympy import symbols
from sympy import sin, cos
from sympy import simplify, expand, factor, trigsimp
from sympy import Eq, solve, solveset, linsolve, nonlinsolve

x, E, e, M = symbols('x E e M')

expr = x**2 + x + 1/x + 1/x**2 
expr = Eq(expr,4)
solve_expr = solveset(expr, x)
print(solve_expr)

e = 0.8
M = 9
expr = E - e * sin(E-M)
expr_new = solveset(expr, E)
print(expr_new)
