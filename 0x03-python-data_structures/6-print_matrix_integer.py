#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            i = 0
            for item in row:
                if i < len(row) - 1:
                    print("{:d}".format(row[i]), end=' ')
                if i == len(row) - 1:
                    print("{:d}".format(row[i]), end='')
                i += 1
            print()
