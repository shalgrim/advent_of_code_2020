from file_ops import read


def find_num_matches(rules, patterns):
    pass


if __name__ == '__main__':
    txt = read(19)
    rule_lines = txt.split('\n\n')[0].split('\n')
    pattern_lines = txt.split('\n\n')[1].split('\n')
    rules = {int(line.split(':')[0]): line.split(':')[1].strip() for line in rule_lines}
    rules[8] = '42 | 42 8'
    rules[11] = '42 31 | 42 11 31'
    patterns = [line.strip() for line in pattern_lines]
    print(find_num_matches(rules, patterns))
