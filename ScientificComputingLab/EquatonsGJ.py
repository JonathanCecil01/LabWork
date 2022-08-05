# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:05:27 2022

@author: 20pt12
"""

import numpy as np
import re


def findAug(equations):
    aug = []
    for equation in equations:
        coeff = re.findall(r'([-?\d]+)', equation)
        coeff =[int(i) for i in coeff]
        aug.append(coeff)
    aug = np.array(aug)
    return aug


def calcnz(matrix):
    nz_pos=[]
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j]!=0:
                nz_pos.append(j)
                break
    return nz_pos
def Rearrange(matrix):
    nz_pos = calcnz(matrix)
    n = matrix.shape[0]
    for i in range(n-1):
        for j in range(n-i-1):
            if nz_pos[j]>nz_pos[j+1]:
                temp = tuple(matrix[j])
                matrix[j]= matrix[j+1] 
                matrix[j+1]=  list(temp)
                nz_pos[j], nz_pos[j+1] = nz_pos[j+1], nz_pos[j]
    return matrix
def make_1(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j]!=0:
                    inverse = 1/matrix[i][j]
                    matrix[i] = np.multiply(inverse, matrix[i])
                    break
    return matrix


def GaussJordan(matrix):
    print(matrix)
    for i in range(matrix.shape[0]):
       matrix = Rearrange(matrix)
       matrix = make_1(matrix)
       print(matrix)
       nz_pos= calcnz(matrix)
       print(nz_pos)
       for j in range(matrix.shape[0]):
           if j!=i:
               matrix[j] = matrix[j]- np.multiply(matrix[j][nz_pos[i]], matrix[i])
               print(matrix)





equations = ['21x+3y+5z = 9','2x-3y+5z = 100']
Augmented = findAug(equations)
GaussJordan(Augmented)


















