from unittest import TestCase

from day15_1 import apply_mask, main as main1


class TestDay15(TestCase):
    def setUp(self):
        self.mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        self.lines = [
            'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
            'mem[8] = 11',
            'mem[7] = 101',
            'mem[8] = 0',
        ]

    def test_apply_mask(self):
        self.assertEqual(73, apply_mask(self.mask, 11))
        self.assertEqual(101, apply_mask(self.mask, 101))
        self.assertEqual(64, apply_mask(self.mask, 0))

    def test_part1(self):
        self.assertEqual(165, main1(self.lines))
