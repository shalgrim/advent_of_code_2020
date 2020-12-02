import re


PATTERN = re.compile(r'(?P<lo>\d+)-(?P<hi>\d+)\s+(?P<letter>[a-z]):\s+(?P<password>\S+)')


def is_valid(group):
    lo = int(group[0])
    hi = int(group[1])
    char = group[2]
    password = group[3]

    return lo <= password.count(char) <= hi


if __name__ == '__main__':
    with open('../data/input02.txt') as f:
        lines = f.readlines()

    groups = [PATTERN.match(line).groups() for line in lines]
    print(sum(is_valid(group) for group in groups))
