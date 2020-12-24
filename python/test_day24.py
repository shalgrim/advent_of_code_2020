from unittest import TestCase

from day24_1 import main
from day24_2 import main as main2


class TestDay24(TestCase):
    def setUp(self):
        with open('../data/test24.txt') as f:
            self.lines = [line.strip() for line in f.readlines()]

    def test_part1(self):
        self.assertEqual(10, main(self.lines))

    def test_part2(self):
        self.assertEqual(15, main2(self.lines, 1))
        self.assertEqual(12, main2(self.lines, 2))
        self.assertEqual(25, main2(self.lines, 3))
        self.assertEqual(14, main2(self.lines, 4))
        self.assertEqual(23, main2(self.lines, 5))
        self.assertEqual(28, main2(self.lines, 6))
        self.assertEqual(41, main2(self.lines, 7))
        self.assertEqual(37, main2(self.lines, 8))
        self.assertEqual(49, main2(self.lines, 9))
        self.assertEqual(37, main2(self.lines, 10))
        self.assertEqual(132, main2(self.lines, 20))
        self.assertEqual(259, main2(self.lines, 30))
        self.assertEqual(406, main2(self.lines, 40))
        self.assertEqual(566, main2(self.lines, 50))
        self.assertEqual(788, main2(self.lines, 60))
        self.assertEqual(1106, main2(self.lines, 70))
        self.assertEqual(1373, main2(self.lines, 80))
        self.assertEqual(1844, main2(self.lines, 90))
        self.assertEqual(2208, main2(self.lines, 100))
