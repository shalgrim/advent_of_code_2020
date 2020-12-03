from math import prod

from day03_1 import count_trees

if __name__ == '__main__':
    with open(f'../data/input03.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    rights = [1, 3, 5, 7, 1]
    downs = [1, 1, 1, 1, 2]
    tree_counts = [
        count_trees(right, down, lines) for right, down in zip(rights, downs)
    ]
    print(prod(tree_counts))
