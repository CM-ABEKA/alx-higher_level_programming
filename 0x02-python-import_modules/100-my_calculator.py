#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argz = sys.argv[1:]
    argc = len(argz)
    for i in argz:
        print(i, end=', ')
    print("argc = {:d} and op = {:s}".format(argc, argz[1]))
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argz[0])
    op = argz[1]
    b = int(argz[2])
    res = 0

    if op == '+':
        res = add(a, b)
        s
        exit(0)
    elif op == '-':
        res = sub(a, b)
        exit(0)
    elif op == "*":
        res = mul(a, b)
        exit(0)
    elif op == '/':
        res = div(a, b)
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} {:d}".format(a, op, b, res))
