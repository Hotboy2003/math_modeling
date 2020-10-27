# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:54:01 2020

@author: admin
"""
from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import Eq, solve, solveset, linsolve, nonlinsolve

n,m,a = symbols('n m a')

n = int(input())
m = int(input())
w = 2

sh = (exp(a) + exp(-a)) / 2
ch = (exp(a) - exp(-a)) / 2

x = (w*sh.subs(a,n))/(ch.subs(a,n) - cos(m))
y = (w*sin(n)) / (ch.subs(a,n) - cos(m))
print(x.subs(a,n).evalf(),y.subs(a,n).evalf())

