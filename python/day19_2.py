import re
from copy import copy
from itertools import product

from day19_1 import generate_possibilities, generate_possibilities_generalized
from file_ops import read

POSSIBILITIES_42 = [
    'bbbbbaab',
    'abbbaaba',
    'abbbabab',
    'abbababa',
    'aaababba',
    'aababbab',
    'aaabbaba',
    'abaabbba',
    'aaaababa',
    'aaaabaab',
    'bbaaaaab',
    'babbaaaa',
    'aabbbaaa',
    'bbabbaab',
    'abbabbba',
    'bbaaabba',
    'bbabbbba',
    'bbbaabab',
    'abaaabba',
    'babbaaba',
    'baaabaaa',
    'abaaaaab',
    'bababaaa',
    'aabaabba',
    'ababaaba',
    'bbbabaab',
    'abbbbaba',
    'babaaaab',
    'babaabab',
    'aabaaaab',
    'baababbb',
    'baaabaab',
    'baaabbaa',
    'aababaab',
    'baabbbaa',
    'bbbbabaa',
    'ababbaaa',
    'aaaabbaa',
    'abbbbbba',
    'bbaababb',
    'aabbbaba',
    'bbabaaaa',
    'ababbbab',
    'aaaaabba',
    'abababab',
    'aaabbbbb',
    'aaabbbba',
    'bbaabbba',
    'abbbaabb',
    'ababbaba',
    'baaababa',
    'abbbbaaa',
    'ababaaaa',
    'aaababab',
    'baaabbba',
    'babbbbbb',
    'abaabaaa',
    'bababbbb',
    'bbbaaaab',
    'bbbababa',
    'baaabbab',
    'bbbabbab',
    'babbbbab',
    'abbbaaaa',
    'abbbbbaa',
    'abaaabab',
    'abbaabba',
    'baababaa',
    'baabbbba',
    'bbbaabaa',
    'bbbabaaa',
    'bbaaaaba',
    'bbbbbbbb',
    'abaabbaa',
    'babaabaa',
    'abbbbaab',
    'babbaabb',
    'bbabbbbb',
    'abbaabbb',
    'bbabbbaa',
    'ababaabb',
    'baaababb',
    'aaaaabbb',
    'abbbbbab',
    'aabbaaba',
    'baaabbbb',
    'aaaabbba',
    'aaaaabab',
    'bbabaaba',
    'bbaabaaa',
    'bbaabbaa',
    'aaabaaba',
    'aaaabaaa',
    'aabbabbb',
    'abbabaab',
    'aabbabaa',
    'abbaaaaa',
    'aaaaaabb',
    'aaabbaaa',
    'bbbaabbb',
    'bbabaabb',
    'baaaabab',
    'bbbbbbab',
    'ababbaab',
    'baabbaab',
    'abaabaab',
    'babaabbb',
    'baabbabb',
    'bababbba',
    'baaaaaba',
    'aabababb',
    'babbbabb',
    'babababa',
    'aabbaaab',
    'bbaaaabb',
    'baabaaab',
    'bbbaaabb',
    'babbabba',
    'babbbbaa',
    'abbabbab',
    'abaababa',
    'bbaabbab',
    'aababbaa',
    'aabbbaab',
    'bbbbbaaa',
    'bbababbb',
    'bbabbaba',
    'babaaaba',
]

POSSIBILITIES_31 = [
    'abaaaabb',
    'aaaaabaa',
    'aabbbabb',
    'ababaaab',
    'abbabbbb',
    'bbaabaab',
    'bbababab',
    'aabaabbb',
    'abbbbbbb',
    'aaaabbbb',
    'aababaaa',
    'baaaabbb',
    'abaaabbb',
    'bbbababb',
    'abbababb',
    'aaabaaab',
    'abaabbab',
    'abbbbabb',
    'aabbbbaa',
    'bbbbaaab',
    'aaabbbab',
    'aaaaaaaa',
    'abababbb',
    'abbabaaa',
    'ababbbbb',
    'baaaabba',
    'baababab',
    'aaababbb',
    'bbbbabab',
    'aabbabba',
    'baaaabaa',
    'bbbbabbb',
    'abbaaaba',
    'aabbbbab',
    'aaabbbaa',
    'bbaaabbb',
    'aabaaaaa',
    'bbabbaaa',
    'aaaababb',
    'aaaabbab',
    'bbaaabab',
    'ababbbaa',
    'aababbba',
    'aaabaaaa',
    'babbaaab',
    'abababba',
    'aaababaa',
    'aabaaabb',
    'babbbaab',
    'bbbabbaa',
    'abababaa',
    'baabaabb',
    'bbbbbabb',
    'abbaaabb',
    'aabbaabb',
    'aabaabaa',
    'abaaaaaa',
    'bbbbabba',
    'bbabaaab',
    'aabbbbba',
    'abbbabbb',
    'bbbbaaba',
    'baaaaabb',
    'babaaabb',
    'bbababaa',
    'aaabbabb',
    'babbabab',
    'baaaaaaa',
    'baababba',
    'bbbbbbba',
    'abaaaaba',
    'ababbbba',
    'abaabbbb',
    'babbabaa',
    'baabbaaa',
    'babbbaaa',
    'bbababba',
    'bbabbbab',
    'abbaaaab',
    'bbbaaaba',
    'babbbbba',
    'aababbbb',
    'bbbaaaaa',
    'baabaaba',
    'bababbaa',
    'bbaaaaaa',
    'aaaaaaab',
    'abbbaaab',
    'baabaaaa',
    'abbabbaa',
    'aabbaaaa',
    'abaababb',
    'babbabbb',
    'abbaabab',
    'babbbaba',
    'babaabba',
    'bbbbbaba',
    'ababbabb',
    'bbbabbbb',
    'aabababa',
    'aabaaaba',
    'bbbbaabb',
    'bbbaabba',
    'aaabaabb',
    'aaabbaab',
    'babaaaaa',
    'babababb',
    'baabbbbb',
    'bbbabbba',
    'baabbbab',
    'bbaabbbb',
    'aabbbbbb',
    'bbaaabaa',
    'abbbabba',
    'aabbabab',
    'bbbbbbaa',
    'bbaababa',
    'aaaaaaba',
    'abbbabaa',
    'bbbbaaaa',
    'baabbaba',
    'baaaaaab',
    'bbabbabb',
    'aabaabab',
    'bababaab',
    'abaaabaa',
    'abbaabaa',
    'bababbab',
]

POSSIBILITIES_11 = [''.join(foo) for foo in product(POSSIBILITIES_42, POSSIBILITIES_31)]

STRING42 = f'((?:{")|(?:".join(POSSIBILITIES_42)}))' + '{2,}'
PATT42 = re.compile(STRING42)

STRING11 = f'((?:{")|(?:".join(POSSIBILITIES_11)}))' + '{2,}'
PATT11 = re.compile(STRING11)


def find_42_matches(pattern):
    return list(PATT42.finditer(pattern))


def find_num_matches(rules, patterns):
    possibilities = generate_possibilities_generalized(rules)
    return len(possibilities.intersection(set(patterns)))


def reducible(pattern):
    return find_42_matches(pattern)


def find_11_matches(pattern):
    return list(PATT11.finditer(pattern))


def reduce(pattern):
    reduced = copy(pattern)
    while reducible(reduced):
        matches_11 = find_11_matches(reduced)
        if matches_11:
            match = matches_11[0]
            end = match.end()
            start = match.start()
            reduced = reduced[: start + 8] + reduced[end - 8 :]
        else:
            matches_42 = find_42_matches(reduced)
            match = matches_42[0]
            end = match.end()
            start = match.start()
            reduced = reduced[:start] + reduced[start + 8 :]

    return reduced


def generate_pattern_8(possibilites_8):
    """rule 8: 42 becomes rule 8: 42 | 8 42"""
    STRING42 = f'^((?:{")|(?:".join(possibilites_8)}))+$'
    PATT42 = re.compile(STRING42)
    return PATT42


def generate_pattern_11(possibilities_42, possibilities_31):
    """rule 11: 42 31 becomes rule 11: 42 31 | 42 11 31"""
    part42 = f'(?:{")|(?:".join(possibilities_42)})'
    part31 = f'(?:{")|(?:".join(possibilities_31)})'
    n1 = f'(?:{part42})(?:{part31})'
    n2 = '(?:' + part42 + '){2}(?:' + part31 + '){2}'
    alln = f'(?:{")|(?:".join([n1, n2])})$'
    return re.compile(alln)


def get_last_11_match(patt11, mycopy):
    last_match = patt11.search(mycopy)
    newer_match = last_match
    while newer_match:
        last_match = newer_match
        newer_match = patt11.search(mycopy, last_match.start() + 1)

    return last_match


def get_11_start_2(pattern, possibilities_42, possibilities_31):
    """rule 11: 42 31 becomes rule 11: 42 31 | 42 11 31"""
    len31 = len(list(possibilities_31)[0])
    working_copy = copy(pattern)
    num_31s_at_end = 0

    if working_copy[-len31:] not in possibilities_31:
        return False

    while working_copy[-len31:] in possibilities_31:
        num_31s_at_end += 1
        working_copy = working_copy[:-len31]

    for i in range(num_31s_at_end):
        if working_copy[-len31:] in possibilities_42:
            working_copy = working_copy[:-len31]
        else:
            return False

    return len(pattern) - len31 * 2 * num_31s_at_end


def get_11_start(pattern, patt11):
    mycopy = copy(pattern)
    while True:
        match = get_last_11_match(patt11, mycopy)
        if not match:
            return False
        if match.end() == len(mycopy):
            return match.start()
        mycopy = mycopy[: match.start()] + mycopy[match.end() :]


def find_num_matches_v3(rules, patterns):
    """because rule 0: 8 11"""
    possibilites_42 = generate_possibilities(rules, 8)
    patt8 = generate_pattern_8(possibilites_42)

    possibilites_31 = generate_possibilities(rules, 31)
    patt11 = generate_pattern_11(possibilites_42, possibilites_31)

    strings_that_match = []

    for pattern in patterns:
        # start11 = get_11_start(pattern, patt11)
        start11 = get_11_start_2(pattern, possibilites_42, possibilites_31)
        if not start11:
            continue

        len42 = len(list(possibilites_42)[0])
        working_copy = copy(pattern[:start11])
        for i in range(len(working_copy) // len42):
            if working_copy[i * len42 : (i + 1) * len42] not in possibilites_42:
                break
        else:
            strings_that_match.append(pattern)

    return len(strings_that_match)


if __name__ == '__main__':
    txt = read(19)
    rule_lines = txt.split('\n\n')[0].split('\n')
    pattern_lines = txt.split('\n\n')[1].split('\n')
    rules = {int(line.split(':')[0]): line.split(':')[1].strip() for line in rule_lines}
    # rules[8] = '42 | 42 8'
    # rules[11] = '42 31 | 42 11 31'
    # rules[8] = (
    #     '42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42 | 42 42 42 42 42 42 | 42 42 42 42 42 42 42 | 42 '
    #     '42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 '
    #     '42 42 42 | 42 42 42 42 42 42 42 42 42 42 42 42'
    # )
    # rules[11] = (
    #     '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31 | '
    #     '42 42 42 42 42 42 31 31 31 31 31 31 | 42 42 42 42 42 42 42 31 31 31 31 31 31 31 | 42 42 42 42 42 42 '
    #     '42 42 31 31 31 31 31 31 31 31'
    # )
    patterns = [line.strip() for line in pattern_lines]
    # print(find_num_matches(rules, patterns))
    possibilites_42 = generate_possibilities(rules, 42)
    possibilites_31 = generate_possibilities(rules, 31)
    print(f'there are {len(possibilites_42)} 42 possibilities')
    for p in possibilites_42:
        print(p)
    print(f'there are {len(possibilites_31)} 31 possibilities')
    for p in possibilites_31:
        print(p)
    print(
        f'there are {len(possibilites_31.intersection(possibilites_42))} possibilities in the intersection'
    )
    # print(find_num_matches(rules, patterns))
    print(find_num_matches_v3(rules, patterns))
