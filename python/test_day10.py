from unittest import TestCase

from day10_1 import main


class TestDay10(TestCase):
    def test_part1(self):
        nums = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self.assertEqual(main(nums), (7, 0, 5))
