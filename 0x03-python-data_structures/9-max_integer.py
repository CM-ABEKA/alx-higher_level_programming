#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_v = my_list[0]
    i = 0
    for x in my_list:
        if x > max_v:
            max_v = x
        i += 1
    return max_v
