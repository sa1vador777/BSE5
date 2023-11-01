#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import prod

def main() -> list[int]:

    numbers_list = [number for number in range(100, 1000)]
    result: list[int] = []
    for element in numbers_list:
        str_element = str(element)
        list_element: list[int] = [int(i) for i in str_element]
        sum_elements = int(sum(list_element))
        prod_element = prod(list_element)
        if sum_elements == prod_element:
            result.append(element)
    return result


if __name__ == "__main__":
    print(main())
