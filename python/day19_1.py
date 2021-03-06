from itertools import product
from file_ops import read

# def matches(pattern, rules, rule_number=0):
#     if not pattern:
#         return True
#
#     rule = rules[rule_number]
#     if rule == '"a"':
#         if pattern[0] == 'a':
#             return matches(pattern[1:], rules, )
#
#     if rule in ['"a"', '"b"']


def generate_possibilities(rules, rule_num=0):
    rule = rules[rule_num]
    if rule == '"a"':
        return set('a')
    elif rule == '"b"':
        return set('b')
    elif '|' not in rule:
        possibilities = []
        for sub_rule_num in [int(num) for num in rule.split()]:
            possibilities.append(generate_possibilities(rules, sub_rule_num))
        return {''.join(foo) for foo in product(*possibilities)}
    else:
        poss1 = []
        poss2 = []
        side1, side2 = rule.split('|')
        for sub_rule_num in [int(num) for num in side1.split()]:
            poss1.append(generate_possibilities(rules, sub_rule_num))

        for sub_rule_num in [int(num) for num in side2.split()]:
            poss2.append(generate_possibilities(rules, sub_rule_num))

        return {''.join(foo) for foo in product(*poss1)} | {
            ''.join(foo) for foo in product(*poss2)
        }


def generate_possibilities_generalized(rules, rule_num=0):
    rule = rules[rule_num]
    if rule == '"a"':
        return set('a')
    elif rule == '"b"':
        return set('b')
    else:
        possibilities_of_possibilities = []
        for side in rule.split('|'):
            these_possibilities = []
            for sub_rule_num in [int(num) for num in side.strip().split()]:
                these_possibilities.append(generate_possibilities_generalized(rules, sub_rule_num))
            possibilities_of_possibilities.append(these_possibilities)

        string_possibilities = [{''.join(foo) for foo in product(*poss)} for poss in possibilities_of_possibilities]
        all_possibilities = set()
        for sp in string_possibilities:
            all_possibilities |= sp

        return all_possibilities


def find_num_matches(rules, patterns):
    possibilities = generate_possibilities(rules)
    return len(possibilities.intersection(set(patterns)))


if __name__ == '__main__':
    txt = read(19)
    rule_lines = txt.split('\n\n')[0].split('\n')
    pattern_lines = txt.split('\n\n')[1].split('\n')
    rules = {int(line.split(':')[0]): line.split(':')[1].strip() for line in rule_lines}
    patterns = [line.strip() for line in pattern_lines]
    print(find_num_matches(rules, patterns))
