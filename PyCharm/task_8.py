#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def geome_mean(*args):
    if args:
        nums = [float(arg) for arg in args]
        return math.prod(nums)**(1/len(nums))
    else:
        return None


if __name__ == '__main__':
    arguments = [i for i in input("Enter the arguments: ").split()]
    print(f"The geometric mean of these arguments is: {geome_mean(*arguments)}")
