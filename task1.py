#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(n: int) -> str:
    if n > 100:
        return f"Введите число меньше 100"
    if int(str(n)[-1]) == 1:
        if n == 11:
            return f"Мне {n} лет"
        return f"Мне {n} год"
    if 1 < int(str(n)[-1]) < 5:
        return f"Мне {n} года"
    return f"Мне {n} лет"


if __name__ == "__main__":
    n = int(input("Введите число от 0 до 100: "))
    print(main(n))
