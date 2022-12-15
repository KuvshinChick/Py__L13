#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_modules(*args):
    if args:
        nums = [int(arg) for arg in args]
        return sum(nums[nums.index(0):len(nums) - 1 - nums[::-1].index(0):])
    else:
        return None


if __name__ == '__main__':
    arguments = [i for i in input("Enter the arguments: ").split()]
    print(f"The sum is: {sum_of_modules(*arguments)}")
