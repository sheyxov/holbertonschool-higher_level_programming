#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    total = 0
    for i in my_list:
        if i not in new:
            new.append(i)
            total = total + i
    return total
