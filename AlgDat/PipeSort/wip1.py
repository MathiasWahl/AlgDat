#!/usr/bin/python3

from sys import stdin


def sort_list(list):
    if len(list) > 3:
        list1 = list[:len(list) // 2]
        list2 = list[len(list)//2:]
        return sort([sort_list(list1), sort_list(list2)])
    if len(list) == 2:
        out = sort([[list[0]],[list[1]]])
        return out
    if len(list) == 3:
        list1 = sort([list[0],list[1]])
        return sort([list1, list[2]])
    if len(list) == 1:
        return list


def sort(list):
    outList = []
    lowlist = list[0]
    highlist = list[1]
    print("Foerste del: ")
    print(lowlist)
    print("andre del: ")
    print(highlist)
    while True:
       try:
        lowlist, highlist = compare(lowlist, highlist)
        outList.append(lowlist[0])
        lowlist.pop(0)

       except Exception:
            for n in lowlist, highlist:
                outList.append(n)
                print(n)
            break

    print("Sortert, riktig liste?: \n" + str(outList))
    return outList

def compare(list1, list2):
    if list1[0] <= list2[0]:
        return list1, list2
    else:
        return list2, list1

def find(A, lower, upper):
    # NOTICE: The result must be returned.
    # SKRIV DIN KODE HER
    print(A)
    i = 0
    low = None
    high = None
    while low is None or high is None:
        if A[i] >= lower and low is None:
            low = A[i]
        if high is None:
            if len(A) == i+1:
                high = A[i]
            elif A[i+1] > upper:
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
