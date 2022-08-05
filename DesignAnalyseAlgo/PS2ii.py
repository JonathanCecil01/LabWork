# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def kthlargest(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k]
    elif len(arr2) == 0:
        return arr1[k]

    mida1 = len(arr1) // 2  
    mida2 = len(arr2) // 2
    if mida1 + mida2 < k:
        if arr1[mida1] > arr2[mida2]:
            return kthlargest(arr1, arr2[mida2+1:], k - mida2 - 1)
        else:
            return kthlargest(arr1[mida1+1:], arr2, k - mida1 - 1)
    else:
        if arr1[mida1] > arr2[mida2]:
            return kthlargest(arr1[:mida1], arr2, k)
        else:
            return kthlargest(arr1, arr2[:mida2], k)

A = [2, 5, 8, 9, 12, 16, 20]
B = [1, 4, 6, 11, 24]
print(kthlargest(A, B, 5))