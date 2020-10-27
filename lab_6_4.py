# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:08:46 2020

@author: admin
"""
from sympy import symbols
from sympy import sin, cos, pi, exp, Abs
from sympy import Eq, solve, solveset, linsolve, nonlinsolve
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
x, y, z = symbols('x y z')


sol = reduce_abs_inequality(Abs(x**2 + 2*x - 3) + 3*(x+1), '<', x)
print(sol)