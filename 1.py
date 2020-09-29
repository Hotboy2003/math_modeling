# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = int(input())
b = int(input())
c = int(input())

D = (b**2) - 4*a*c

if D<0:
    print('Нет корней')
elif D==0:
    print('Один корень')
    x = (-b + D**0.5) / (2*a)
    print(x)
elif D>0:
    print('Два корня')
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print(x1, x2)
    
