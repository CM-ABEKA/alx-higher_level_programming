#!/usr/bin/python3
""" Module Inheritance """


class MyList(list):
    ''' inherits from list object '''

    def print_sorted(self):
        ''' print list in sorted ascending order '''
        if issubclass(MyList, list):
            print(sorted(self))
