#!/usr/bin/python3
'''
    module prints the first and last name
'''


def say_my_name(first_name, last_name=""):
    '''
        This Function Prints

        `My name is <first name> <last name>`

        Args:
            @first_name: a string
            @second_name: a string

        Raises:
            TypeError:
            -- first_name must be a string or
                last_name must be a string

    '''
    errMsg1 = 'first_name must be a string'
    errMsg2 = 'last_name must be a string'
    if type(first_name) is not str:
        raise TypeError(errMsg1)
    if type(last_name) is not str:
        raise TypeError(errMsg2)

    print("My name is {} {}".format(first_name, last_name))
