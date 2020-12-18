from unittest import TestCase

from day18_1 import evaluate
from day18_2 import evaluate as evaluate2
from file_ops import readlines


class TestDay18(TestCase):
    def test_evaluate(self):
        self.assertEqual(71, evaluate('1 + 2 * 3 + 4 * 5 + 6'))
        self.assertEqual(51, evaluate('1 + (2 * 3) + (4 * (5 + 6))'))
        self.assertEqual(26, evaluate('2 * 3 + (4 * 5)'))
        self.assertEqual(437, evaluate('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
        self.assertEqual(12240, evaluate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
        self.assertEqual(13632, evaluate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))

    def test_part1(self):
        self.assertEqual(1451467526514, sum([evaluate(line) for line in readlines(18)]))

    def test_evaluate2(self):
        self.assertEqual(231, evaluate2('1 + 2 * 3 + 4 * 5 + 6'))
        self.assertEqual(51, evaluate2('1 + (2 * 3) + (4 * (5 + 6))'))
        self.assertEqual(46, evaluate2('2 * 3 + (4 * 5)'))
        self.assertEqual(1445, evaluate2('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
        self.assertEqual(669060, evaluate2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
        self.assertEqual(23340, evaluate2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))
        self.assertEqual(4012416, evaluate2('9 * 6 * 3 * 8 * ((8 * 4 * 2 * 6) + 3 * 8)'))
