#!/usr/bin/python3
i = 0
for i in range(i, 100):
    if i != 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
