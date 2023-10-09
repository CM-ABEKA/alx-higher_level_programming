#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argz = sys.argv[1:]
    argc = len(argz)
    i = 0
    if argc == 0:
        print("{:d} arguments.".format(argc))
    if argc >= 1:
        s = ''
        if argc > 1:
            s = 's'
        print("{:d} argument{}:".format(argc, s))
        for a in argz:
            print("{:d}: {}".format(i + 1, argz[i]))
            i += 1
