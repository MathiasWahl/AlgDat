#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        #Dictionry: key er bokstav. value er ny node. hvis ikke noe, lag.
        self.posi = []


    def getChildren(self):
        out = "Has " + str(len(self.barn)) + " Children: "
        out += str(self.barn.keys())
        return out

    def getPosition(self):
        return self.posi


def bygg(aList):
    topNode = Node()
    for tup in aList:
        #print("ord: " + tup[0])
        aboveNode = topNode
        newNode = None
        for letter in tup[0]:
            #print("Leter etter: " + letter)
            if letter in aboveNode.barn.keys():
                aboveNode = aboveNode.barn[letter]
                newNode = aboveNode
            else:
                newNode = Node()
                aboveNode.barn.update({letter: newNode})
                aboveNode = newNode
        newNode.posi.append(tup[1])

    return topNode

def posisjoner(word, index, node):
    foundpositions = index
    aboveNode = node
    for char in word:
        if char in aboveNode.barn.keys():
            aboveNode = aboveNode.barn[char]
        elif char == " ":
            ind = word.index(" ")
            try:
                aboveNode = aboveNode.barn[word[ind+1]]
            except:
                return []
        elif char == "?":
            ind = word.index("?")
            a = word[ind + 1:]
            if len(a) != 0:
                for childkey in aboveNode.barn:
                    returned = (posisjoner(a,[],aboveNode.barn[childkey]))
                    for i in returned:
                        foundpositions.append(i)
                return foundpositions
            elif len(a) == 0:
                for childkey in aboveNode.barn:
                    for posi in aboveNode.barn[childkey].posi:
                        foundpositions.append(posi)
                return foundpositions
    for i in aboveNode.posi:
        foundpositions.append(i)
    return foundpositions

def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            outString = sokeord + ": "
            posi = posisjoner(sokeord, [], toppnode)
            posi.sort()
            for p in posi:
                outString += str(p) + " "
            print(outString)
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()
