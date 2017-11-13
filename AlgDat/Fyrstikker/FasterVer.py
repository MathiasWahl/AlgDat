from math import floor
def mergework(A, p, q, r):
    n1 = q - p
    n2 = r - q
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j]
    L[n1] = 999999999999999
    R[n2] = 999999999999999
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
    list = [1,3,2,5,4,6,2,6,8,4,9,10,8]
    mergesort(list, 0, len(list))
    print(list)

if __name__ == "__main__":
    main()
