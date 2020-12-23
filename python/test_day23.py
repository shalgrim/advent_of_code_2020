from unittest import TestCase

from day23_1 import convert_cups_to_answer, main, play_game


class TestDay23(TestCase):
    def test_convert_cups_to_answer(self):
        self.assertEqual(
            '92658374', convert_cups_to_answer([5, 8, 3, 7, 4, 1, 9, 2, 6])
        )

    def test_play_game(self):
        self.assertEqual(
            [3, 2, 8, 9, 1, 5, 4, 6, 7], play_game([3, 8, 9, 1, 2, 5, 4, 6, 7], 1)
        )
        self.assertEqual(
            [5, 8, 3, 7, 4, 1, 9, 2, 6], play_game([3, 8, 9, 1, 2, 5, 4, 6, 7], 10)
        )

    def test_part1(self):
        self.assertEqual('92658374', main('389125467', 10))
        self.assertEqual('67384529', main('389125467', 100))
