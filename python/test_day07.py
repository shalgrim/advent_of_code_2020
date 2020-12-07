from unittest import TestCase
from day07_1 import main


class TestDay07(TestCase):
    def test_part1(self):
        self.assertEqual(
            set(['bright white', 'muted yellow', 'dark orange', 'light red']),
            main('../data/test07.txt'),
        )
