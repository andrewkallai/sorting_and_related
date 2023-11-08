#!/usr/bin/env python3

import pdb

def partition(A, p, r):
    x = A[r]
    i = p - 1
    print(r-p)
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            (A[i], A[j]) = (A[j], A[i])
    (A[i + 1], A[r]) = (A[r], A[i + 1])
    return i + 1

def quickSort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        print("Partition made")
        print("||||||||||||||||>")
        #print(p, r, r - p + 1)
        #print("before left")
        #print(p, q-1)
        quickSort(A, p, q -1)
        #print(p, q-1)
        #print("after left")
        #print("before right")
        #print(q+1, r)
        quickSort(A, q+1, r)
        #print(q+1, r)
        #print("after right")


#data = [1, 7, 4, 1, 10, 9, -2]
data = [5, 3, 5, 8, 5, 9, 2, 6, 9, 7, 3, 1, 4, 1]
#print(data)
#pdb.set_trace() 
size = len(data)
#partition(data, 0, size - 1) 
quickSort(data, 0, size - 1)
 
print(data)
