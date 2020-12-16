import math

from day16_1 import parse_text, get_invalid_values, is_invalid
from file_ops import read


def is_valid_ticket(ticket, rules):
    return not get_invalid_values(ticket, rules)


def get_possible_fields(values, names_and_rules):
    possibilities = []

    for name, rules in names_and_rules:
        if all(not is_invalid(v, [rules]) for v in values):
            possibilities.append(name)
    return possibilities


def remove_name(on, names_and_rules):
    try:
        index = [nar[0] for nar in names_and_rules].index(on)
    except ValueError:
        return names_and_rules
        index = names.index(on)

    del names_and_rules[index]
    return names_and_rules


def order_field_names(field_names, rules, tickets):
    ordered_names = [None] * len(field_names)
    names_and_rules = list(zip(field_names, rules))

    while None in ordered_names:
        for i in range(len(field_names)):
            possible_fields = get_possible_fields(
                [ticket[i] for ticket in tickets], names_and_rules
            )

            if len(possible_fields) == 1:
                name = possible_fields[0]
                ordered_names[i] = possible_fields[0]

        for on in ordered_names:
            if on:
                names_and_rules = remove_name(on, names_and_rules)

    return ordered_names


def get_ordered_field_names(txt):
    field_names, rules, my_ticket, other_tickets = parse_text(txt)
    valid_tickets = [
        ticket for ticket in other_tickets if is_valid_ticket(ticket, rules)
    ]
    ordered_field_names = order_field_names(field_names, rules, valid_tickets)

    return ordered_field_names


def main(txt):
    ordered_field_names = get_ordered_field_names(txt)
    _, _, my_ticket, _ = parse_text(txt)  # TODO: remove redundant work being done
    departure_indexes = [
        i for i, ofn in enumerate(ordered_field_names) if 'departure' in ofn
    ]
    departure_values = [my_ticket[i] for i in departure_indexes]
    return math.prod(departure_values)


if __name__ == '__main__':
    print(main(read(16)))
