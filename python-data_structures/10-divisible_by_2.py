#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    c = []
    for i in my_list:
        if i % 2 == 0:
            c.append(True)
        else:
            c.append(False)
    return c
