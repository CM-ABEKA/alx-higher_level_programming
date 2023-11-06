#!/usr/bin/python3
''' inheritance modules '''


def inherits_from(obj, a_class):
    ''' checks if an object is an inherited instance of a
        class.

        Args:
            @obj: the object
            @a_class: class to match type of object to

        Returns:
            True if inherited
            False if not inherited
    '''

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
