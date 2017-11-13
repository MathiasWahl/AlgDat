from sys import stdin

Inf = float(1e3000)

def mst(nm):
    from heapq import heappop, heappush
    h = []
    t = [0] * n
    w = 0
    for i in nl[0]: heappush(h, i)
    t[0] = 1
    for i in range(1, n):
        if not 0 in t: break
        while h:
            e = heappop(h)
            m = e[1]
            if t[m]: continue
            t[m] = 1
            if w < e[0]: w = e[0]
            for e in nl[m]:
                if not t[e[1]]: heappush(h, e)
            break
    return w


def main():
    lines = []
    file = open("/Users/Mathias/PycharmProjects/AlgDat/Pathbuilding/input",'r')
    #for str in stdin:
    for str in file.readlines():
        lines.append(str.strip())
    n = len(lines)
    neighbour_matrix = [None] * n
    node = 0
    print(lines)
    print(neighbour_matrix)
    for line in lines:
        neighbour_matrix[node] = [Inf] * n
        for k in line.split():
            data = k.split(':')
            neighbour = int(data[0])
            weight = int(data[1])
            neighbour_matrix[node][neighbour] = weight
        node += 1
    print (mst(neighbour_matrix))

if __name__ == '__main__':
    main()
