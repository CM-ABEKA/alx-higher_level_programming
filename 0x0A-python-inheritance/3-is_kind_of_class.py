#!/usr/bin/python3
''' Checks class instances '''


def is_kind_of_class(obj, a_class):
    ''' checks if obj is the same class or inherit
        from a_class
    '''

    return isinstance(obj, a_class)
