from copy import copy

from day21_1 import make_food, cant_be_allergen
from file_ops import readlines


def main(lines):
    foods = [make_food(line) for line in lines]
    not_possibly_allergens = cant_be_allergen(foods)
    all_ingredients = set()
    all_allergens = set()

    for food in foods:
        all_ingredients.update(food[0])
        all_allergens.update(food[1])

    answers = {}
    for allergen in all_allergens:
        possibilities = set()
        for food in foods:
            if allergen in food[1]:
                if not possibilities:
                    possibilities = copy(food[0])
                else:
                    possibilities.intersection_update(food[0])

        answers[allergen] = possibilities

    final_answers = {}
    while answers:
        for k, v in answers.items():
            if len(v) == 1:
                final_answers[k] = v.pop()

        for k, v in final_answers.items():
            if k in answers:
                del answers[k]
            for k2, v2 in answers.items():
                if v in v2:
                    v2.remove(v)

    return ','.join([v for k, v in sorted(final_answers.items())])


if __name__ == '__main__':
    lines = readlines(21)
    print(main(lines))
