#!/usr/bin/env python3

import math
import pdb

def parent(i):
    return math.floor(i / 2)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    print(A, i, heap_size) 
    if not(l >= len(A)):
        print("1 comparison")
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if not(r >= len(A)):
        print("1 comparison 2nd")
    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        #print(A[i], i, A[largest], largest)
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)

def build_max_heap(A, heap_size):
    A_length = len(A)
    n = (A_length // 2) -1
    #pdb.set_trace();
    for i in range(n, -1, -1):
        max_heapify(A, i, heap_size)

def heapsort(A):
    heap_size = len(A) 
    build_max_heap(A, heap_size)
    for i in range(len(A)-1,0,-1):
        #print(A[i], i, A[0], 0)
        A[i], A[0] = A[0], A[i]
        heap_size = heap_size - 1
        max_heapify(A, 0, heap_size)

if __name__ == "__main__":
    #A = [11, 6, 5, 0, 8, 2, 7]
    #A = [3, 5, 4, 6, 2, 1, 5]
    #A = [3, 3, 2, 1]
    #A = [21, 20, 20, 12, 11, 8, 7]
    A = [27, 18, 4, 5, 22, 95, 35, 11, 17]
    #A= [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    #build_max_heap(A, len(A))
    #print(A)
    A = [27, 18, 4, 5, 22, 95, 35, 11, 17]
    heapsort(A)
    print(A)

