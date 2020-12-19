from copy import copy
from unittest import TestCase
from day19_1 import generate_possibilities, find_num_matches
from day19_2 import find_num_matches as find_num_matches2


class TestDay19Part1(TestCase):
    def setUp(self):
        self.rules = {
            0: '4 1 5',
            1: '2 3 | 3 2',
            2: '4 4 | 5 5',
            3: '4 5 | 5 4',
            4: '"a"',
            5: '"b"',
        }

        self.patterns = ['ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb']

    def test_generate_possibilities(self):
        self.assertEqual(set(['a']), generate_possibilities(self.rules, 4))
        self.assertEqual(set(['b']), generate_possibilities(self.rules, 5))
        self.assertEqual(set(['ab', 'ba']), generate_possibilities(self.rules, 3))
        self.assertEqual(set(['aa', 'bb']), generate_possibilities(self.rules, 2))
        self.assertEqual(
            set(['aaab', 'aaba', 'bbab', 'bbba', 'abaa', 'abbb', 'baaa', 'babb']),
            generate_possibilities(self.rules, 1),
        )
        self.assertEqual(
            set(
                [
                    'aaaabb',
                    'aaabab',
                    'abbabb',
                    'abbbab',
                    'aabaab',
                    'aabbbb',
                    'abaaab',
                    'ababbb',
                ]
            ),
            generate_possibilities(self.rules, 0),
        )

    def test_find_num_matches(self):
        self.assertEqual(2, find_num_matches(self.rules, self.patterns))


class TestDay19Part2(TestCase):
    def setUp(self):
        self.pre_rules = {
            42: '9 14 | 10 1',
            9: '14 27 | 1 26',
            10: '23 14 | 28 1',
            1: '"a"',
            11: '42 31',
            5: '1 14 | 15 1',
            19: '14 1 | 14 14',
            12: '24 14 | 19 1',
            16: '15 1 | 14 14',
            31: '14 17 | 1 13',
            6: '14 14 | 1 14',
            2: '1 24 | 14 4',
            0: '8 11',
            13: '14 3 | 1 12',
            15: '1 | 14',
            17: '14 2 | 1 7',
            23: '25 1 | 22 14',
            28: '16 1',
            4: '1 1',
            20: '14 14 | 1 15',
            3: '5 14 | 16 1',
            27: '1 6 | 14 18',
            14: '"b"',
            21: '14 1 | 1 14',
            25: '1 1 | 1 14',
            22: '14 14',
            8: '42',
            26: '14 22 | 1 20',
            18: '15 15',
            7: '14 5 | 1 21',
            24: '14 1',
        }

        self.patterns = [
            'abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa',
            'bbabbbbaabaabba',
            'babbbbaabbbbbabbbbbbaabaaabaaa',
            'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
            'bbbbbbbaaaabbbbaaabbabaaa',
            'bbbababbbbaaaaaaaabbababaaababaabab',
            'ababaaaaaabaaab',
            'ababaaaaabbbaba',
            'baabbaaaabbaaaababbaababb',
            'abbbbabbbbaaaababbbbbbaaaababb',
            'aaaaabbaabaaaaababaa',
            'aaaabbaaaabbaaa',
            'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
            'babaaabbbaaabaababbaabababaaab',
            'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba',
        ]

        self.post_rules = copy(self.pre_rules)
        self.post_rules[8] = '42 | 42 8'
        self.post_rules[11] = '42 31 | 42 11 31'

    def test_find_num_matches(self):
        self.assertEqual(3, find_num_matches(self.pre_rules, self.patterns))

    def test_find_num_matches_v2(self):
        self.assertEqual(12, find_num_matches2(self.post_rules, self.patterns))
