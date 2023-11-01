#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import factorial

def main(x: float, e: float = 1e-10):
    result = 0
    term = x
    n = 1
    while abs(term) > e:
        result += term
        n += 1
        term = ((-1) ** (n * (x ** (2 * n + 1)))) / ((2 * n + 1) * factorial(2 * n + 1))
    return result


if __name__ == "__main__":
    pass
    x = float(input("Введите значение x: "))
    result = main(x)
    print(f"Si({x}) = {result}")
