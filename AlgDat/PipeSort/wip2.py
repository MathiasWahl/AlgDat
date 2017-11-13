#!/usr/bin/python3

from sys import stdin


def sort_list(list):
    if len(list) > 3:
        list1 = list[:len(list) // 2]
        list2 = list[len(list)//2:]
        finalsort = sort([sort_list(list1), sort_list(list2)])
        return finalsort
    if len(list) == 2:
        out = sort([[list[0]],[list[1]]])
        return out
    if len(list) == 3:
        list1 = sort([[list[0]],[list[1]]])
        return sort([list1, [list[2]]])
    if len(list) == 1:
        return list


def sort(list):
    sortedlist = []
    lowlist = list[0]
    highlist = list[1]
    while True:
        try:
            lowlist, highlist = compare(lowlist, highlist)
            sortedlist.append(lowlist[0])
            lowlist.pop(0)
        except Exception:
            if len(lowlist) > len(highlist):
                for n in lowlist:
                    sortedlist.append(n)
            else:
                for n in highlist:
                    sortedlist.append(n)
            break
    return sortedlist


def compare(list1, list2):
    if list1[0] <= list2[0]:
        return list1, list2
    else:
        return list2, list1

def find(A, lower, upper):
    i = 0
    low = None
    high = None
    if len(A) == 2:
        return A
    if lower < A[0]:
        low = A[0]
    while high is None:
        if A[i+1] > lower and low is None:
            low = A[i]
        if high is None:
            if len(A) == i+1:
                high = A[i]
            elif A[i] >= upper:
                high = A[i]
        i += 1
    return [low, high]





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
