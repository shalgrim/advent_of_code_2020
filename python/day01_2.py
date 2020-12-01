from itertools import combinations


if __name__ == '__main__':
    with open('../data/input01.txt') as f:
        lines = f.readlines()

    nums = [int(line.strip()) for line in lines]
    for combo in combinations(nums, 3):
        if sum(combo) == 2020:
            break

    print(combo[0]*combo[1]*combo[2])
