from file_ops import read


def parse_field_names(lines):
    return [line.split(':')[0] for line in lines]


def parse_rules(lines):
    rules = []
    for line in lines:
        back_half = line.strip().split(': ')[1]
        ranges = back_half.split(' or ')
        ranges = [range.split('-') for range in ranges]
        intized_ranges = []
        for range in ranges:
            intized_ranges.append((int(range[0]), int(range[1])))
        rules.append(intized_ranges)
    return rules


def parse_ticket(line):
    return [int(v) for v in line.split(',')]


def is_invalid(v, rules):
    for rule in rules:
        for range in rule:
            if range[0] <= v <= range[1]:
                return False
    return True


def get_invalid_values(ticket, rules):
    return [v for v in ticket if is_invalid(v, rules)]


def main(text):
    _, rules, my_ticket, other_tickets = parse_text(text)
    invalid_values = []
    for ot in other_tickets:
        invalid_values += get_invalid_values(ot, rules)

    return sum(invalid_values)


def parse_text(text):
    rules, my_ticket, other_tickets = text.split('\n\n')
    field_names = [line.split(':')[0] for line in rules.split('\n')]
    rules = parse_rules(rules.split('\n'))
    my_ticket = parse_ticket(my_ticket.split('\n')[1])
    other_tickets = [parse_ticket(line) for line in other_tickets.strip().split('\n')[1:]]
    return field_names, rules, my_ticket, other_tickets


if __name__ == '__main__':
    print(main(read(16)))
