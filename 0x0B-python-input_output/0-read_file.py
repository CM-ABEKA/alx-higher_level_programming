#!/usr/bin/python3
''' Module for reading files '''


def read_file(filename=""):
    ''' Function Reads File With UTF8 Encoding '''

    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
