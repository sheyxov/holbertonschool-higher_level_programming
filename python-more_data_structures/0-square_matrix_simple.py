#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    kv = []
    for i in matrix:
        raw = []
        for j in i:
            raw.append(j * j)
        kv.append(raw)
    return kv
