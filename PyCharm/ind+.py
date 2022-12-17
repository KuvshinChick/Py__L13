#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_modules(*args):
    if args:
        min_num = max(args)
        for i in args:
            if abs(i) < min_num:
                min_num = abs(i)
                i_min = args.index(i)
        return sum(args[i_min + 1::])
    else:
        return None


if __name__ == '__main__':
    arguments = [int(i) for i in input("Enter the arguments: ").split()]
    print(f"The sum is: {sum_of_modules(*arguments)}")
