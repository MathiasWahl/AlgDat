#!/usr/bin/python3
from sys import stdin
from math import *


def find(A, lower, upper):
    lowindex = binsok(A, lower)
    highindex = binsok(A, upper)
    if A[lowindex] > lower and lowindex != 0:
        lowindex -= 1
    if A[highindex] < upper and highindex != len(A) - 1:
        highindex += 1
    return [A[lowindex], A[highindex]]


def binsok(A, value):
    l = 0
    r = len(A) - 1
    while l <= r:
        x = (l + r) // 2
        if value == A[x]:
            break
        elif value < A[x]:
            r = x - 1
        else:
            l = x + 1
    return x

def sort_list(list):
    mergesort(list, 0, len(list))
    return list


def mergework(A, p, q, r):
    n1 = q - p
    n2 = r - q
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    greatnum = 1000
    for i in range(n1):
        var = A[p + i]
        L[i] = var
        greatnum += var
    for j in range(n2):
        var = A[q + j]
        R[j] = var
        greatnum += var
    L[n1] = greatnum
    R[n2] = greatnum
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergesort(A, p, r):
    if p < (r - 1):
        q = (p + r)//2
        mergesort(A, p, q)
        mergesort(A, q, r)
        mergework(A, p, q, r)


def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
