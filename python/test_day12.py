from unittest import TestCase

from day12_1 import main
from day12_2 import main as main2


class TestDay12(TestCase):
    def test_part1(self):
        lines = ['F10', 'N3', 'F7', 'R90', 'F11']
        self.assertEqual(25, main(lines))

    def test_part2(self):
        lines = ['F10', 'N3', 'F7', 'R90', 'F11']
        self.assertEqual(286, main2(lines))
