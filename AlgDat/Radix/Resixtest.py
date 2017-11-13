
def radSort(A = []):
    A = [56, 94, 54, 92, 100, 9]
    temp = [[]]*10
    for num in A:
        temp[num % 10].append(num)
    print(temp)


def main():
    radSort()

if __name__ == '__main__':
    main()
