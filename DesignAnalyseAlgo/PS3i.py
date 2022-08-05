# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:30:23 2022

@author: 20pt12
"""

trees = [20, 15, 10, 17]
k=7
min= 0
max = 19
mid = (max+min)//2
left = min
right = max
while(left<right):
    print("Middle Value : ", mid)
    
    sumls = [i-mid for i in trees if i> mid]
    print(sumls)
    print(sum(sumls))
    if sum(sumls)>k:
        left = mid+1
    elif sum(sumls)<k:
        right = mid-1
    elif sum(sumls)==k:
        print("Tree Cut Perfectly")
        break
    mid = (left+right)//2