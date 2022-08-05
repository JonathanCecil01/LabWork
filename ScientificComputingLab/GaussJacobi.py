# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 13:58:46 2022

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
def GaussJacobi(matrix):
    n = matrix.shape[1]-1
    x = [0]*n
    for i in range(0, 30):
        x = repetition(matrix, x)
    return x
def repetition(matrix, x):
    n = matrix.shape[1]-1
    constant = []
    for i in range(matrix.shape[0]):
        constant.append(matrix[i][3])
    for j in range(n):
        d = constant[j]
        for i in range(n):
            if(j!=i):
                d-=matrix[j][i]*x[i]
        x[j] = d/matrix[j][j]
    return x
        
        


equations = ['21x+3y+5z = 9','2x-3y+5z = 100', '8x+3y+7z = 109']
Augmented = findAug(equations)
#print(Augmented)
Answers = GaussJacobi(Augmented)
Answers = [round(i, 2) for i in Answers]
print(Answers)