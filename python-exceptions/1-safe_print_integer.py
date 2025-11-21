#!/usr/bin/python3
def safe_print_integer(value):
    try:
        i = "{:d}".format(value)
        print(i)
        return True
    except (ValueError, TypeError) as e:
        return False
