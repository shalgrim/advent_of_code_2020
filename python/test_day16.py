from unittest import TestCase

from day16_1 import main, get_invalid_values, is_invalid


class TestDay16(TestCase):
    def setUp(self):
        self.lines = [
            'class: 1-3 or 5-7',
            'row: 6-11 or 33-44',
            'seat: 13-40 or 45-50',
            '',
            'your ticket:',
            '7,1,14',
            '',
            'nearby tickets:',
            '7,3,47',
            '40,4,50',
            '55,2,20',
            '38,6,12',
        ]
        self.rules = [[(1, 3), (5, 7)], [(6, 11), (33, 44)], [(13, 40), (45, 50)]]

    def test_is_invalid(self):
        self.assertFalse(is_invalid(7, self.rules))

    def test_get_invalid_values(self):
        self.assertEqual([], get_invalid_values([7, 1, 14], self.rules))
        self.assertEqual([4], get_invalid_values([40, 4, 50], self.rules))
        self.assertEqual([55], get_invalid_values([55, 2, 20], self.rules))

    def test_part1(self):
        self.assertEqual(71, main('\n'.join(self.lines)))
