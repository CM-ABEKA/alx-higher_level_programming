#!/usr/bin/python3
''' matrix module '''


def matrix_divided(matrix, div):
    '''
        matrix_divided  
        ==============

        divides elements in matrix with div
        -----------------------------------
        Arguments:
            @matrix: the matrix
            -- Must be list of lists
            -- The values must be integers or floats
            @div: the value to divide with
            -- Must be and integer or float
            -- The division is rounded off to 
             decimal places.
        Returns:
            -- The result is returned in a new matrix.
        Raises:
            -- TypeError: matrix not as requirement
            -- ZeroDivisionError: `div` is equal to `0`.
    '''
    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    mtx_type_err = 'matrix must be a matrix (list of lists) of integers/floats'
    mtx_row_err = 'Each row of the matrix must have the same size'
    try:
        mtrx_iter = iter(matrix)
    except TypeError:
        raise TypeError(mtx_type_err)
    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(mtx_row_err)
        for item in lists:
            if not isinstance(item, (int, float)):
                raise TypeError(mtx_type_err)

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
