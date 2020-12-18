from unittest import TestCase

from day18_1 import evaluate


class TestDay18(TestCase):
    def test_evaluate(self):
        self.assertEqual(71, evaluate('1 + 2 * 3 + 4 * 5 + 6'))
        self.assertEqual(51, evaluate('1 + (2 * 3) + (4 * (5 + 6))'))
        self.assertEqual(26, evaluate('2 * 3 + (4 * 5)'))
        self.assertEqual(437, evaluate('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
        self.assertEqual(12240, evaluate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
        self.assertEqual(13632, evaluate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))
