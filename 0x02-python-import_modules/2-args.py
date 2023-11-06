#!/usr/bin/python3
import sys

if __name__ == "__main":
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(count))

    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
