#!/usr/bin/python3
def uppercase(str):
    diff = ord('a') - ord('A')
    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            x = chr(ord(x) - diff)
        print("{}".format(x), end='')
    print('')
