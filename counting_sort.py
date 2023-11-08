#!/usr/bin/env python3
import pdb

def Counting_Sort(A):
    #init B array
    n = len(A)
    B = [None] * n
    #define k
    k = max(A) + 1 
    # init C array
    C = [0] * k 
    pdb.set_trace()
    for i in range(0, n):
        C[A[i]] += 1
    print(A)
    print(C)
    print("a")

    # cummulative C
    for i in range(1, k):
        C[i] += C[i - 1]
    print(C)
    print("b")

    # place the elements in output array
    i = n - 1
    while i >= 0:
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
        i -= 1
        print(B)
        print(C)
        print("c-e")

    # Copy sorted elements
    #for i in range(0, n):
    #    A[i] = B[i]
    return B

array = [2, 5, 3, 0, 2, 3, 0, 3]
#array = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
print("The original array is: ", array)
array = Counting_Sort(array)
print("Array after sorting is: ", array)
