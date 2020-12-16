from unittest import TestCase

from day16_1 import main, get_invalid_values, is_invalid
from day16_2 import is_valid_ticket, get_ordered_field_names


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

    def test_is_valid_ticket(self):
        self.assertTrue(is_valid_ticket([7, 1, 14], self.rules))
        self.assertFalse(is_valid_ticket([40, 4, 50], self.rules))
        self.assertFalse(is_valid_ticket([55, 2, 20], self.rules))
        self.assertFalse(is_valid_ticket([38, 6, 12], self.rules))

    def test_get_ordered_field_names(self):
        self.assertEqual(
            ['row', 'class', 'seat'],
            get_ordered_field_names(
                "class: 0-1 or 4-19\nrow: 0-5 or 8-19\nseat: 0-13 or 16-19\n\n"
                "your ticket:\n11,12,13\n\n"
                "nearby tickets:\n3,9,18\n15,1,5\n5,14,9"
            ),
        )
