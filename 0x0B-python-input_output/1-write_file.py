#!/usr/bin/python3
''' Module writes string to a text file '''


def write_file(filename="", text=""):
    ''' Writes string to a text file and returns
        number of characters written

        @filename: name of file
        @text: the string to be written

    '''
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
