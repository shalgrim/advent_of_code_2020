from collections import defaultdict
from copy import copy

from file_ops import readlines


def make_food(line):
    ingredients = set(line.split('(')[0].split())
    allergens = set(allergen.strip() for allergen in line.split('contains ')[1][:-1].split(','))
    return ingredients, allergens


def cant_be_allergen(foods):
    all_ingredients = set()
    all_allergens = set()

    for food in foods:
        all_ingredients.update(food[0])
        all_allergens.update(food[1])

    allergen_possibilities = {}

    for allergen in all_allergens:
        for food in foods:
            if allergen in food[1]:
                if allergen not in allergen_possibilities:
                    allergen_possibilities[allergen] = copy(food[0])
                else:
                    allergen_possibilities[allergen].intersection_update(food[0])

    potential_allergens = set()
    for p in allergen_possibilities.values():
        potential_allergens.update(p)

    return all_ingredients.difference(potential_allergens)


def main(lines):
    foods = [make_food(line) for line in lines]
    not_possibly_allergens = cant_be_allergen(foods)
    count = 0
    for food in foods:
        count += len(food[0].intersection(not_possibly_allergens))
    return count


if __name__ == '__main__':
    lines = readlines(21)
    print(main(lines))
