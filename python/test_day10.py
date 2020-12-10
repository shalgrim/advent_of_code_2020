from unittest import TestCase

from day10_1 import main
from day10_2 import count_arrangements


class TestDay10(TestCase):
    def test_part1(self):
        nums = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self.assertEqual(main(nums), (7, 0, 5))

    def test_part2(self):
        nums = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self.assertEqual(count_arrangements(nums + [22]), 8)

    def test_part2_2(self):
        nums = [
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3,
        ]
        self.assertEqual(count_arrangements(nums + [max(nums) + 3]), 19208)
