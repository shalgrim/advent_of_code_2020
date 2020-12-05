from unittest import TestCase
from day05_1 import get_row, get_pass_id


class TestDay05(TestCase):
    def test_get_row(self):
        self.assertEqual(get_row('FBFBBFF'), 44)
        self.assertEqual(get_row('BFFFBBF'), 70)
        self.assertEqual(get_row('FFFBBBF'), 14)
        self.assertEqual(get_row('BBFFBBF'), 102)

    def test_get_pass_id(self):
        self.assertEqual(get_pass_id('FBFBBFFRLR'), 357)
        self.assertEqual(get_pass_id('BFFFBBFRRR'), 567)
        self.assertEqual(get_pass_id('FFFBBBFRRR'), 119)
        self.assertEqual(get_pass_id('BBFFBBFRLL'), 820)
