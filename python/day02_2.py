from day02_1 import HI, LETTER, LO, PWD, count_valid
from file_ops import readlines


def is_valid(groupdict):
    first = int(groupdict[LO]) - 1
    second = int(groupdict[HI]) - 1
    letter = groupdict[LETTER]
    password = groupdict[PWD]

    return (password[first] == letter) != (password[second] == letter)


if __name__ == '__main__':
    lines = readlines(2)
    print(count_valid(lines, is_valid))
