import re
from collections import defaultdict

NO_CONTAIN_PATTERN = re.compile(r'(?P<container>.+?) bags contain no other bags.')
CONTAIN_PATTERN = re.compile(r'(?P<container>.+?) bags contain (?P<contained>.+)\.')
SUB_CONTAIN_PATTERN = re.compile(r'(?P<amount>\d+) (?P<bagtype>.+) bag.*')


def create_dicts(filename):
    with open(filename) as f:
        rules = [line.strip() for line in f.readlines()]

    contain = defaultdict(list)
    contained_by = defaultdict(list)

    for rule in rules:
        if match := NO_CONTAIN_PATTERN.match(rule):
            continue
        else:
            match = CONTAIN_PATTERN.match(rule)
            container = match.group('container')
            contained = match.group('contained').split(',')
            for ctd in contained:
                submatch = SUB_CONTAIN_PATTERN.search(ctd)
                contain[container].append((int(submatch.group('amount')), submatch.group('bagtype')))
                contained_by[submatch.group('bagtype')].append(container)
    return contain, contained_by


def main(filename):
    contain, contained_by = create_dicts(filename)
    bag_types = set(contained_by['shiny gold'])
    new_size = len(bag_types)
    old_size = 0
    while old_size != new_size:
        old_size = new_size
        new_bag_types = set()
        for bt in bag_types:
            new_bag_types.update(set(contained_by[bt]))

        bag_types.update(new_bag_types)
        new_size = len(bag_types)

    return bag_types


if __name__ == '__main__':
    print(len(main('../data/input07.txt')))
