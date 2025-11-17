#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # all arguments except script name
    total = 0

    for arg in args:
        total += int(arg)  # cast each argument to int and add

    print(total)
