#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    for group in decks:
        if not len(group) == 1:
            mergesort(group)





def mergework(A, p, q, r):
    n1 = q - p
    n2 = r - q
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j]
    L[n1] = 99999999999
    R[n2] = 99999999999
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergesort(A, p = 0, r = len(A)):
    if p < (r - 1):
        q = (p + r)//2
        mergesort(A, p, q)
        mergesort(A, q, r)
        mergework(A, p, q, r)





def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()
