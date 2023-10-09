#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argz = sys.argv[1:]
    result = 0
    for a in argz:
        result += int(a)
    print("{}".format(result))
