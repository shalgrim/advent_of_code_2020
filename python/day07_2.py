import re
from collections import defaultdict

from day07_1 import create_dicts


def get_contained(amount, bag_type, contain):
    answer = []
    for t in contain[bag_type]:
        this_amount = amount * t[0]
        this_bag_type = t[1]
        answer.append((this_amount, this_bag_type))
        answer += get_contained(this_amount, this_bag_type, contain)
    return answer


def main(filename):
    contain, contained_by = create_dicts(filename)
    contained = get_contained(1, 'shiny gold', contain)
    return sum([c[0] for c in contained])


if __name__ == '__main__':
    print(main('../data/input07.txt'))
