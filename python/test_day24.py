from unittest import TestCase

from day24_1 import main


class TestDay24(TestCase):
    def setUp(self):
        with open('../data/test24.txt') as f:
            self.lines = [line.strip() for line in f.readlines()]

    def test_part1(self):
        self.assertEqual(10, main(self.lines))
