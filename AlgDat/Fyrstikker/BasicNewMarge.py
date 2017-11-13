

def merge(list):
    if len(list) > 3:
        list1 = list[:len(list) // 2]
        list2 = list[len(list)//2:]
        return sort([merge(list1), merge(list2)])
    if len(list) == 2:
        out = sort([list[0],list[1]])
        return out
    if len(list) == 3:
        list1 = sort([list[0],list[1]])
        return sort([list1, list[2]])


def sort(list):
    outList = []
    lowlist = list[0]
    highlist = list[1]
    i = 0
    while True:
       try:
        lowlist, highlist = compare(lowlist, highlist)
        outList.append(lowlist[0])
        lowlist.pop(0)

       except Exception:
            for n in lowlist, highlist:
                outList += n
            break

    return outList


def main():
    myList = [1, 3, 6, 99, 200]
    print(merge(myList))


def compare(list1, list2):
    if list1[0] <= list2[0]:
        return list1, list2
    else:
        return list2, list1


if __name__ == "__main__":
    main()
