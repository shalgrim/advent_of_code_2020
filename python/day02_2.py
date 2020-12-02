from day02_1 import PATTERN


def is_valid(group):
    first = int(group[0]) - 1
    second = int(group[1]) - 1
    char = group[2]
    password = group[3]

    return (password[first] == char) != (password[second] == char)


if __name__ == '__main__':
    with open('../data/input02.txt') as f:
        lines = f.readlines()

    groups = [PATTERN.match(line).groups() for line in lines]
    print(sum(is_valid(group) for group in groups))
