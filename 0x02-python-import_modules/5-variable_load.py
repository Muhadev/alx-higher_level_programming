#!/usr/bin/python3

if __name__ == "__main__":
    from variable_load_5 import a  # Import the variable 'a' from variable_load_5.py
    if a >= 0:
        sign = ""
    else:
        sign = "-"
        a = abs(a)

    print(a)
