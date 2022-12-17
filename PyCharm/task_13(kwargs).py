#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вывести стоимость блюд в том или ином заведении


def print_menu(cafe, **dish):
    print(f"Cafe Name: {cafe}")
    for dish_name, cost in dish.items():
        print(f"{dish_name}: {cost} $")


if __name__ == '__main__':
    print_menu(
        "Cafe_1",
        fish_soup=5,
        meat=8,
        beef=10,
        rice=2
    )
    print_menu(
        "Cafe_2",
        fish_soup=6,
        chicken=3,
        salad=5,
        dessert=3
    )
