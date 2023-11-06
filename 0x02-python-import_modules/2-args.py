#!/usr/bin/python3
def print_str(str):
    print("{}".format(str))

if __name__ == "__main":
    import sys

    num_args = len(sys.argv)
    if num_args == 1:
        print("0 arguments.")
    elif num_args == 2:
        print("1 arguments:")
        print("{:d}: ".format(1), end="")
        print_str(str(sys.argv[1]))
    elif num_args > 2:
        print("{} arguments:".format(num_args - 1))

    for i in range(1, num_args):
        print("{:d}: ".format(i), end="")
        print_str(str(sys.argv[i]))
