from unittest import TestCase

from file_ops import read
from day20_1 import main
from day20_2 import main as main2


class TestDay20(TestCase):
    def setUp(self):
        with open('../data/test20.txt') as f:
            self.txt = f.read()

    def test_part1(self):
        """
        Solution given on AoC is (Flipped180 is the new Vertical)
        1951 Vertical, 2311 Vertical, 3079 Normal
        2729 Vertical, 1427 Vertical, 2473 Flipped90
        2971 ??, 1489 ??, 1171 ??
        But based on my search space I end up with the equivalent
        1951 ROT90 2729 ROT90 2971 ROT90
        2311 ROT90 1427 ROT90 1489 ROT90
        3079 FLIPPED270 2473 ROT180 1171 ROT270
        """
        self.assertEqual(20899048083289, main(self.txt))

    def test_part2(self):
        self.assertEqual(273, main2(self.txt))
