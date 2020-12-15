from unittest import TestCase

from day15_1 import play_game


class TestDay15(TestCase):
    def test_part1(self):
        self.assertEqual(0, play_game([0, 3, 6], 4))
        self.assertEqual(3, play_game([0, 3, 6], 5))
        self.assertEqual(3, play_game([0, 3, 6], 6))
        self.assertEqual(1, play_game([0, 3, 6], 7))
        self.assertEqual(0, play_game([0, 3, 6], 8))
        self.assertEqual(4, play_game([0, 3, 6], 9))
        self.assertEqual(0, play_game([0, 3, 6], 10))
        self.assertEqual(436, play_game([0, 3, 6], 2020))
