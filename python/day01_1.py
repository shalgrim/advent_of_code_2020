from math import prod
from itertools import combinations


def day_1(filename, combo_length):
    with open(filename) as f:
        nums = [int(line.strip()) for line in f.readlines()]

    for combo in combinations(nums, combo_length):
        if sum(combo) == 2020:
            break

    return prod(combo)


if __name__ == '__main__':
    print(day_1('../data/input01.txt', 2))
