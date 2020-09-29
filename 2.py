# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:30:57 2020

@author: student
"""

a = float(input())
b = float(input())
c = float(input())

if (a+b)<=c or (a+c)<=b or (b+c)<=a:
    print('Такого треугольника не существует')
else:
    print('Такой треугольник существует')
    if a==b and c==b:
        print('Треугольник равносторонний')
    elif a!=b and b!=c:
        print('Треугольник разносторонний')
    elif a==b or b==c or c==a:
        print('Треугольник равнобедренный')