from unittest import TestCase
from day19_1 import generate_possibilities, find_num_matches


class TestDay19(TestCase):
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
