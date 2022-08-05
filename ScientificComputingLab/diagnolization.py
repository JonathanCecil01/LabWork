# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:39:16 2022

@author: 20pt12
"""

import numpy as np
import sympy as sp

def diagnolize(matrix):
    for i in range(matrix.shape[0]):
        x = matrix[i][i]
        for j in range(matrix.shape[0]):
            if(matrix[j][i]!=0 and j>i):
                inv = matrix[j][i]/x
                matrix[j] = matrix[j]-np.multiply(matrix[i], inv) 
    for i in range(matrix.shape[0]):
        k = matrix.shape[0]-i-1
        x = matrix[k][k]
        #print(x)
        for j in range(matrix.shape[0]):
            if(matrix[j][k]!=0 and j<k):
                inv = matrix[j][k]/x
                matrix[j] = matrix[j]-np.multiply(matrix[k], inv)
    print(matrix)
matrix = [[-10.0, 11.0, -6.0], [-15.0, 16.0, -10.0], [-3.0, 3.0, -2.0]]
matrix = np.array(matrix)
diagnolize(matrix)