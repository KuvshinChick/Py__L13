#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_modules(*args):
    if args:
        nums = [abs(int(arg)) for arg in args]
        return sum(nums[nums.index(min(nums)) + 1::])
    else:
        return None


if __name__ == '__main__':
    arguments = [i for i in input("Enter the arguments: ").split()]
    print(f"The sum is: {sum_of_modules(*arguments)}")