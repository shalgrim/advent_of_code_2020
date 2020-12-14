from unittest import TestCase

from day14_1 import apply_mask, main as main1
from day14_2 import main as main2, addresses_to_update, apply_mask_version_2


class TestDay14(TestCase):
    def test_apply_mask(self):
        mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        self.assertEqual(73, apply_mask(mask, 11))
        self.assertEqual(101, apply_mask(mask, 101))
        self.assertEqual(64, apply_mask(mask, 0))

    def test_part1(self):
        lines = [
            'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
            'mem[8] = 11',
            'mem[7] = 101',
            'mem[8] = 0',
        ]
        self.assertEqual(165, main1(lines))

    def test_apply_mask_version_2(self):
        self.assertEqual(
            '000000000000000000000000000000X1101X',
            apply_mask_version_2('000000000000000000000000000000X1001X', 42),
        )
        self.assertEqual(
            '00000000000000000000000000000001X0XX',
            apply_mask_version_2('00000000000000000000000000000000X0XX', 26),
        )

    def test_addresses_to_update(self):
        mask = '000000000000000000000000000000X1001X'
        self.assertEqual(set([26, 27, 58, 59]), addresses_to_update(mask, 42))
        mask = '00000000000000000000000000000000X0XX'
        self.assertEqual(
            set([16, 17, 18, 19, 24, 25, 26, 27]), addresses_to_update(mask, 26)
        )

    def test_part2(self):
        lines = [
            'mask = 000000000000000000000000000000X1001X',
            'mem[42] = 100',
            'mask = 00000000000000000000000000000000X0XX',
            'mem[26] = 1',
        ]
        self.assertEqual(208, main2(lines))
