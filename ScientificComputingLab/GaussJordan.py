# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
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

'''
matrix = [[0, 3, -6, 6, 4, -5], [-3, 7, 8, -5, 8, 9], [3, -9, 12, -9, 6, 15]]
matrix = np.array(matrix)
GaussJordan(matrix)
'''