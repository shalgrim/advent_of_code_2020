import os

if __name__ == '__main__':
    print(os.getcwd())
    with open('data/input04.txt') as f:
        txt = f.read()

    passports = txt.split('\n\n')
    fields = [p.split() for p in passports]
    dictized = []
    for field in fields:
        new_dict = {field_item.split(':')[0]: field_item.split(':')[1] for field_item in field}
        dictized.append(new_dict)
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passports = []

    for a_dict in dictized:
        if all(rf in a_dict.keys() for rf in required_fields):
            valid_passports.append(a_dict)

    print(len(valid_passports))
