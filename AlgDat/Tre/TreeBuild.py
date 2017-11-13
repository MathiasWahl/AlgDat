


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
    print(aboveNode)
    for char in word:
        if char in aboveNode.barn.keys():
            aboveNode = aboveNode.barn[char]
        elif char == "?":
            ind = word.index("?")
            a = word[ind + 1:]
            if len(a) != 0:
                for childkey in aboveNode.barn:
                    returned = (posisjoner(a,[],aboveNode.barn[childkey]))
                    for i in returned:
                        foundpositions.append(i)
    for i in aboveNode.posi:
        foundpositions.append(i)
    return foundpositions



def main():
    minliste = [("hete", 0), ("hele", 5), ("heter",10)]
    topnode = bygg(minliste)
    print(topnode.barn)

    #va = topnode.barn["h"].barn["e"].barn["t"].barn["e"].barn["r"]

    #print(va.getChildren())
    #print(va.getPosition())
    b = posisjoner("???e",[],topnode)
    print(b)

if __name__ == '__main__':
    main()

# (Bokstav : Ny node)

