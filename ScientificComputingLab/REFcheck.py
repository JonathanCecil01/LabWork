# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:46:42 2022

@author: 20pt12
"""
import numpy as np

def isRREF(nonzeroes):
    element = 1
    for i in nonzeroes:
        if i!=element:
            print("Not in RREF")
            return
    print("Given Matrix is in RREF")
def IsREF(matrix):
    leadings = []
    leading_loc =-1
    nz_pos = -1
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j]!=0 and i==0:
                leading_loc = j
                leadings.append(matrix[i][j])
                break
            if matrix[i][j]!=0:
                nz_pos=j
                if(nz_pos<=leading_loc):
                    print("Matrix not in REF")
                    return
                leadings.append(matrix[i][j])
    print("Th given Matrix is in REF")
    isRREF(leadings)

#matrix = [[0, -2, 2],[0, 0, 1]]
matrix = [[1, 2, 0, 3, 0], [1, 0, 1, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
matrix = np.array(matrix)
IsREF(matrix)