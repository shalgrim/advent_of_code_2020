from day04_1 import dictize_em, REQUIRED_FIELDS


def is_valid_passport(a_dict):
    if any(rf not in a_dict.keys() for rf in REQUIRED_FIELDS):
        return False

    try:
        if len(a_dict['byr']) != 4:
            return False
        birth_year = int(a_dict['byr'])
        if birth_year < 1920 or birth_year > 2002:
            return False
    except ValueError:
        return False

    try:
        if len(a_dict['iyr']) != 4:
            return False
        issue_year = int(a_dict['iyr'])
        if issue_year < 2010 or issue_year > 2020:
            return False
    except ValueError:
        return False

    try:
        if len(a_dict['eyr']) != 4:
            return False
        exp_year = int(a_dict['eyr'])
        if exp_year < 2020 or exp_year > 2030:
            return False
    except ValueError:
        return False

    try:
        units = a_dict['hgt'][-2:]
        if units not in ['cm', 'in']:
            return False
        height_val = int(a_dict['hgt'][:-2])

        if units == 'cm' and (height_val < 150 or height_val > 193):
            return False
        elif units == 'in' and (height_val < 59 or height_val > 76):
            return False
    except (IndexError, ValueError):
        return False

    if len(a_dict['hcl']) != 7:
        return False
    try:
        hcl = a_dict['hcl']
        if hcl[0] != '#':
            return False
        if any(
            c
            not in [
                '0',
                '1',
                '2',
                '3',
                '4',
                '5',
                '6',
                '7',
                '8',
                '9',
                'a',
                'b',
                'c',
                'd',
                'e',
                'f',
            ]
            for c in hcl[1:]
        ):
            return False
    except IndexError:
        return False

    if a_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    try:
        passport_id = int(a_dict['pid'])
    except ValueError:
        return False

    if len(a_dict['pid']) != 9:
        return False

    return True


if __name__ == '__main__':
    with open('../data/input04.txt') as f:
        txt = f.read()
    dictized = dictize_em(txt)
    valid_passports = []

    for a_dict in dictized:
        if is_valid_passport(a_dict):
            valid_passports.append(a_dict)

    print(len(valid_passports))  # 16 and 133 are incorrect
