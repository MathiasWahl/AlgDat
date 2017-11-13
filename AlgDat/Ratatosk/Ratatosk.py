#!/usr/bin/python3

from sys import stdin


class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0


def dfs(root):
    myStack = [root]
    while True:
        index = len(myStack) - 1
        current_node = myStack[index]
        if current_node.ratatosk:
            return index
        if current_node.next_child == len(current_node.child):
            myStack.pop()
        else:
            myStack.append(current_node.child[current_node.next_child])
            current_node.next_child += 1



def bfs(root):
    myQueue = [(root, 0)]
    while len(myQueue)> 0:
        current_node, depth = myQueue.pop()
        if current_node.ratatosk:
            return depth
        for child in current_node.child:
            myQueue.append((child, depth + 1))



def main():
    #stdin = open("/Users/Mathias/PycharmProjects/AlgDat/Ratatosk/InputExample",'r')
    function = stdin.readline().strip()
    number_of_nodes = int(stdin.readline())
    nodes = []
    for i in range(number_of_nodes):
        nodes.append(Node())
    start_node = nodes[int(stdin.readline())]
    ratatosk_node = nodes[int(stdin.readline())]
    ratatosk_node.ratatosk = True
    for line in stdin:
        number = line.split()
        temp_node = nodes[int(number.pop(0))]
        for child_number in number:
            temp_node.child.append(nodes[int(child_number)])

    if function == 'dfs':
        print(dfs(start_node))
    elif function == 'bfs':
        print(bfs(start_node))
    elif function == 'velg':
        print(bfs(start_node))




if __name__ == '__main__':
    main()
