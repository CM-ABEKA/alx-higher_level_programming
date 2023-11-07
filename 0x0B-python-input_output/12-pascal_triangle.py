#!/usr/bin/python3
''' Define the Pascals triangle '''


def pascal_triangle(n):
    '''Represent Pascal Triangle of size n'''

    if n <= 0:
        return []

    triang = [[1]]
    while len(triang) != n:
        tr = triang[-1]
        tmp = [1]
        for i in range(len(tri) - 1]):
            tmp.append(tri[i] = tri[i] + tri[i + 1])
        tmp.append(1)
        triang.append(tmp)
    return triang
