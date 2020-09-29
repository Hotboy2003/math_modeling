# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:41:36 2020

@author: student
"""

import numpy as np

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

a1 = np.ndarray(shape=(n,m))
a2 = np.ndarray(shape=(n,m))
a3 = np.ndarray(shape=(n,m))

for i in range(n):
    for j in range(m):
        a1[i,j] = int(input('Введите элемент первого массива: {},{} '.format(i, j)))
        a2[i,j] = int(input('Введите элемент второго массива: {},{} '.format(i, j)))

for i in range(n):
    for j in range(m):
        if a1[i,j] >= a2[i,j]:
            a3[i,j]=a1[i,j]
        elif a2[i,j] > a1[i,j]:
            a3[i,j] = a2[i,j]
 
print(a3)