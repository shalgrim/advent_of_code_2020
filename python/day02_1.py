import re

from file_ops import readlines

LO = 'lo'
HI = 'hi'
LETTER = 'letter'
PWD = 'pwd'
PATTERN = re.compile(
    rf'(?P<{LO}>\d+)-(?P<{HI}>\d+)\s+(?P<{LETTER}>[a-z]):\s+(?P<{PWD}>\S+)'
)


def is_valid(groupdict):
    lo = int(groupdict[LO])
    hi = int(groupdict[HI])
    letter = groupdict[LETTER]
    password = groupdict[PWD]

    return lo <= password.count(letter) <= hi


def count_valid(lines, is_valid_algorithm):
    groups = [PATTERN.match(line).groupdict() for line in lines]
    return sum(is_valid_algorithm(group) for group in groups)


if __name__ == '__main__':
    lines = readlines(2)
    print(count_valid(lines, is_valid))
