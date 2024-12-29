import math


def calculate_easter_bread_ingredients(bread_count):
    total_sugar = 0
    total_flour = 0
    max_sugar = 0
    max_flour = 0

    for _ in range(bread_count):
        sugar_used = int(input())
        flour_used = int(input())

        total_sugar += sugar_used
        total_flour += flour_used

        if sugar_used > max_sugar:
            max_sugar = sugar_used
        if flour_used > max_flour:
            max_flour = flour_used

    sugar_packages = math.ceil(total_sugar / 950)
    flour_packages = math.ceil(total_flour / 750)

    print(f'Sugar: {sugar_packages}')
    print(f'Flour: {flour_packages}')
    print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')


breads = int(input())
calculate_easter_bread_ingredients(breads)
