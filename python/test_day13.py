from unittest import TestCase
from day13_2 import main, does_work


class TestDay13(TestCase):
    def test_does_work(self):
        self.assertTrue(does_work(0, 7, 1068781))
        self.assertTrue(does_work(1, 13, 1068781))
        self.assertTrue(does_work(4, 59, 1068781))
        self.assertTrue(does_work(6, 31, 1068781))
        self.assertTrue(does_work(7, 19, 1068781))

    def test_part2(self):
        line_two = '7,13,x,x,59,x,31,19'
        self.assertEqual(1068781, main(line_two))