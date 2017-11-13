#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(deckz):
    worklist = mergework(deckz)
    prettystring = ""
    for c in worklist:
        prettystring += c[1]
    return prettystring


def mergework(decks):
    if len(decks) > 3:
        return sort([mergework(decks[len(decks)//2:]), mergework(decks[:len(decks)//2])])
    elif len(decks) == 3:
        return sort([sort([decks[0], decks[1]]), decks[2]])
    else:
        return sort([decks[0], decks[1]])


def sort(mylist):
    outlist = []
    lowlist = mylist[0]
    highlist = mylist[1]
    while True:
        try:
            lowlist, highlist = compare(lowlist, highlist)
            outlist.append(lowlist[0])
            lowlist.pop(0)

        except Exception:
            for n in lowlist, highlist:
                outlist += n
            break
    return outlist


def compare(list1, list2):
    if list1[0] <= list2[0]:
        return list1, list2
    else:
        return list2, list1


def main():
    # Read input.
    decks = []
    # tester = ["i:1,3,5,8", "n:2", "t:4,7", "a:6", "v:9"] #Fjern
    for line in stdin:
        # for line in tester:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()
