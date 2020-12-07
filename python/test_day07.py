from unittest import TestCase
from day07_1 import main as main1
from day07_2 import main as main2


class TestDay07(TestCase):
    def test_part1(self):
        self.assertEqual(
            set(['bright white', 'muted yellow', 'dark orange', 'light red']),
            main1('../data/test07_1.txt'),
        )
        self.assertEqual(179, len(main1('../data/input07.txt')))

    def test_part2(self):
        self.assertEqual(126, main2('../data/test07_2.txt'))
