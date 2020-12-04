REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def dictize_em(txt):
    passports = txt.split('\n\n')
    fields = [p.split() for p in passports]
    dictized = []

    for field in fields:
        new_dict = {field_item.split(':')[0]: field_item.split(':')[1] for field_item in field}
        dictized.append(new_dict)

    return dictized


if __name__ == '__main__':
    with open('data/input04.txt') as f:
        txt = f.read()

    dictized = dictize_em(txt)
    valid_passports = []

    for a_dict in dictized:
        if all(rf in a_dict.keys() for rf in REQUIRED_FIELDS):
            valid_passports.append(a_dict)

    print(len(valid_passports))
