#!/usr/bin/python3
'''
    module prints text with 2 new lines
    after characters . ? and :
'''


def text_indentation(text):
    '''
    prints text with 2 new lines after 
    characters . ? and :
    
    Args:
        @text: must be string

    there should be no space at the beginning or
    at the end of each printed line

    Raises:
    TypeError: text must be a string
    '''
    if type(text) is not str:
        raise TypeError('text must be a string')
    split_char = ['.', '?', ':']
    temp = ""
    for char in text:
        if char not in split_char:
            temp += char
        elif char in split_char:
            temp += char
            print(temp.strip())
            print()
            temp = ""
