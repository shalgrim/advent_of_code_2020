from unittest import TestCase
from day11_1 import main
from day11_2 import main as main2


class TestDay11(TestCase):
    def setUp(self):
        self.lines = [
            'L.LL.LL.LL',
            'LLLLLLL.LL',
            'L.L.L..L..',
            'LLLL.LL.LL',
            'L.LL.LL.LL',
            'L.LLLLL.LL',
            '..L.L.....',
            'LLLLLLLLLL',
            'L.LLLLLL.L',
            'L.LLLLL.LL',
        ]
    def test_part1(self):
        self.assertEqual(37, main(self.lines))

    def test_part2(self):
        self.assertEqual(26, main2(self.lines))

