#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a = 0
    b = 0
    for key in a_dictionary:
        if b is None or a_dictionary[key] > b:
            b = a_dictionary[key]
            a = key
    return a
