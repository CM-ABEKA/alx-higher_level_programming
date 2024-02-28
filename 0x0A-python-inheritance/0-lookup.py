#!/usr/bin/python3
""" Module Returns Attributes and Methods """


def lookup(obj):
    ''' This function returns the attr and methods
        of an object.

        usage: lookup(obj)

        @obj: the object to check
    '''
    return (dir(obj))
