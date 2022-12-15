#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmon_mean(*args):
    if args:
        # Сразу получаю перевернутые дроби 1/n
        nums = [1/int(arg) for arg in args]
        return len(nums)/sum(nums)
    else:
        return None


if __name__ == '__main__':
    arguments = [i for i in input("Enter the arguments: ").split()]
    print(f"The harmonic mean of these arguments is: {harmon_mean(*arguments)}")
