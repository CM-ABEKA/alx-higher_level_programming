#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = list(map(lambda m: [a ** 2 for a in m], matrix))
    return squares
