# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import sympy as sp
from sympy import symbols, Eq, solve, Poly
def get_identity(a):
    identity = []
    row_i = []
    for i in range(a):
        for j in range(a):
            if(j==i):
                row_i.append(1)
            else:
                row_i.append(0)
        identity.append(row_i)
        row_i = []
    identity = np.array(identity)
    return identity

def eigen_vector(e_val):
    A=[]
    A_row=[]
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            A_row.append(e_val*identity[i][j] - matrix[i][j])
        A.append(A_row)
        A_row=[]
    X = []
    x_row = []
    for i in range(matrix.shape[0]):
        for j in range(0, 1):
            x_row.append(symbols('x'+str(i)))
        X.append(x_row)
        x_row=[]
    X = sp.Matrix(X)
    A = sp.Matrix(A)
    equations = A*X
    eqs=[]
    for i in equations:
        eqs.append(i)
    sol = sp.linsolve(eqs, tuple(X))
    solution = []
    for i in sol:
        for j in i:
            solution.append(j)

    solution2 =[]
    for expr in solution:
        if type(expr)!=sp.core.numbers.Zero:
            equi =1*expr
            dicto = dict(equi.as_coefficients_dict())
            for i in dicto:
                value = (dicto[i])
                solution2.append(value)
        else:
            solution2.append(0)
    
    return solution2
    
def eigen_val(matrix, identity):
    x = symbols('x')
    A=[]
    A_row=[]
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            A_row.append(x*identity[i][j] - matrix[i][j])
        A.append(A_row)
        A_row=[]
    A = sp.Matrix(A)
    det = A.det()
    sol = solve(det)
    return sol


matrix = [[4, 0, 1],[-2, 1, 0],[-2, 0, 1]]
#matrix = [[-5, 2], [-7, 4]]
matrix = np.array(matrix)
identity = get_identity(matrix.shape[0])
eigen_values = eigen_val(matrix, identity)
print("Eigen Values : ", eigen_values)
eigen_vectors=[]
for i in eigen_values:
    eigen_vectors.append(eigen_vector(i))
print("Eigen Vectors : ")
for i in eigen_vectors:
    print(i)











