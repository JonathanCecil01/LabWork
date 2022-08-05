# -*- coding: utf-8 -*-
#Augmented Matrix
import re
equations = []
'''
n = int(input("Please Enter th no of equations"))
for i in range(0, n):
    equation = input()
    equations.append(equation)
'''
equations = ['21x+3y+5z = 9','2x+3y+5z = 100']
number = ''
aug = []
for equation in equations:
    coeff = re.findall(r'([\d]+)', equation)
    aug.append(coeff)
print(aug)

