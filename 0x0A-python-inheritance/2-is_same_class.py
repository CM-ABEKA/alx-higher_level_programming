#!/usr/bin/python3
''' Module returns true if object same instance '''


def is_same_class(obj, a_class):
    ''' checks if instance of obj is same as that
        of the specified class.
    '''

    if type(obj) is a_class:
        return True
    else:
        return False
