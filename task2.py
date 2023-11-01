#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(year: int) -> str:
    remainder: int = year % 60
    animals = {
        "5": "Мышь",
        "10": "Корова",
        "15": "Тигр",
        "20": "Заяц",
        "25": "Дракон",
        "30": "Змея",
        "35": "Лошадь",
        "40": "Овца",
        "45": "Обезьяна",
        "50": "Курица",
        "55": "Собака",
        "60": "Свинья"
    }
    colors = {
        "12": "Зеленый",
        "24": "Красный",
        "36": "Белый",
        "48": "Желтый",
        "60": "Черный"
    }
    my_animal: str = ""
    for remainder_y, animal in animals.items():
        if remainder < int(remainder_y):
            my_animal += f"{animal} "
    my_animal: str = my_animal.split(' ')[0]
    my_color: str = ""
    for remainder_y, color in colors.items():
        if remainder < int(remainder_y):
            my_color += f"{color} "
    my_color: str = my_color.split(' ')[0]
    return f"Год: {my_color} {my_animal}"

if __name__ == "__main__":
    year = int(input("Введите год: "))
    print(main(year))
