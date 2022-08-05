# -*- coding: utf-8 -*-


import numpy as np
import sympy as sp
from sympy import symbols, Eq, solve, Poly

def orthocheck(ev1, ev2):
    ev1 = np.array(ev1)
    ev2 = np.array(ev2)
    ev1.transpose()
    if sum(np.multiply(ev1, ev2))==0:
        return True
    else:
        return False

def normalize(evs,matrix):
    evs = np.array(evs)
    A =[]
    row=[]
    for i in evs:
        temp = sum([j**2 for j in i])
        row =np.multiply(i, 1/temp**0.5)
        row = [round(i, 1) for i in row]
        A.append(row)
    A = np.array(A)
    #print(A)
    A_trans = A.transpose()
    #print(A_trans)
    temp = np.multiply(A_trans, matrix)
    D = np.multiply(temp, A)
    print(D)
        
        

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


matrix = [[-1, 7, -1],[0, 1, 0],[0, 15, -2]]
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
flag = True
for i in range(len(eigen_vectors)):
    for j in range(0,i):
        if(orthocheck(eigen_vector(i), eigen_vector(j))):
            continue
        else:
            print("Sorry Canonical not possible since eigens are not orthogonal")
            flag = False
            break

if(flag):
    normalize(eigen_vectors, matrix)









