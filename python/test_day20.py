from unittest import TestCase

from file_ops import read
from day20_1 import main


class TestDay20(TestCase):
    def setUp(self):
        with open('../data/test20.txt') as f:
            self.txt = f.read()

    def test_part1(self):
        """
        Solution is (Flipped180 is the new Vertical)
        1951 Vertical, 2311 Vertical, 3079 Normal
        2729 Vertical, 1427 Vertical, 2473 Flipped90
        ??, ??, ??
        Even after adding eight arrangements, I'm still not getting a solved square
        So some stepping through is called for
        """
        self.assertEqual(20899048083289, main(self.txt))
