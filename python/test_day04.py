from unittest import TestCase

from day04_1 import dictize_em
from day04_2 import is_valid_passport


class TestDay04(TestCase):
    def test_part2(self):
        astr = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
        dictized = dictize_em(astr)
        for d in dictized:
            print(is_valid_passport(d))
        self.assertTrue(all(is_valid_passport(d) for d in dictized))
