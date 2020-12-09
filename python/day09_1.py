from itertools import combinations

from file_ops import readlines


def is_valid(num, prev_25):
    return num in (sum(combo) for combo in combinations(prev_25, 2))


if __name__ == '__main__':
    nums = readlines(9, int)
    prev_25 = []
    for num in nums:
        if len(prev_25) == 25 and not is_valid(num, prev_25):
            break
        prev_25.append(num)
        if len(prev_25) > 25:
            prev_25.pop(0)
    print(num)
