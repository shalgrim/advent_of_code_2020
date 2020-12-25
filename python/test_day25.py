from unittest import TestCase

from day25_1 import calc_loop_size, calc_encryption_key


class TestDay25(TestCase):
    def test_calc_loop_size(self):
        self.assertEqual(8, calc_loop_size(5764801))
        self.assertEqual(11, calc_loop_size(17807724))

    def test_calc_encryption_key(self):
        self.assertEqual((14897079, 14897079), calc_encryption_key(5764801, 17807724))
