from math import prod
from itertools import combinations
from file_ops import readlines


def day_1(combo_length):
    nums = readlines(1, int)
    for combo in combinations(nums, combo_length):
        if sum(combo) == 2020:
            break

    return prod(combo)


if __name__ == '__main__':
    print(day_1(2))
