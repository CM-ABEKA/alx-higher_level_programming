#!/usr/bin/python3
''' Module appends a string '''


def append_write(filename="", text=""):
    ''' Appends a string at end of a text file
        with `utf-8` encoding.
    '''

    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text))
