from sys import stdin, stderr

def best_path(nm, prob):
    nodes = [(None, prob[0])] + [(None, 0)] * (len(prob) - 1)
    finished_nodes = []
    for nodenumber in range(len(nm)):
        for next_pointer in range(len(nm[nodenumber])):
            if nm[nodenumber][next_pointer] == 1:
                if next_pointer not in finished_nodes:
                    if nodes[next_pointer][0] == None:
                        nodes[next_pointer] = (nodenumber, nodes[nodenumber][1] * prob[next_pointer])
                    elif nodes[next_pointer][1] < nodes[nodenumber][1] * prob[next_pointer]:
                        nodes[next_pointer] = (nodenumber, nodes[nodenumber][1] * prob[next_pointer])
        finished_nodes.append(nodenumber)
    return findpath(nodes, len(prob) - 1)

def findpath(nodes, n):
    outStr = "" + str(n)
    nextone = nodes[n][0]
    if nextone == None:
        return "0"
    while nextone is not None:
        outStr = str(nextone) + "-" + outStr
        nextone = nodes[nextone][0]
    if outStr[0] != "0":
        return "0"
    return outStr


def main():
    myFile = open("/Users/Mathias/PycharmProjects/AlgDat/Mummy/input.txt",'r')
    #n = int(stdin.readline())
    lines = myFile.readlines()
    n = int(lines[0])
    probabilities = [float(x) for x in lines[1].split()]
    neighbour_matrix = []
    for line in lines[2:]:
        neighbour_row = [0] * n
        neighbours = [int(neighbour) for neighbour in line.split()]
        for neighbour in neighbours:
            neighbour_row[neighbour] = 1
        neighbour_matrix.append(neighbour_row)
    print (best_path(neighbour_matrix, probabilities))



if __name__ == '__main__':
    main()
