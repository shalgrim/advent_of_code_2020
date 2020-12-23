from unittest import TestCase

from day21_1 import make_food, cant_be_allergen, main
from day21_2 import main as main2


class TestDay21(TestCase):
    def setUp(self):
        self.lines = [
            'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
            'trh fvjkl sbzzf mxmxvkd (contains dairy)',
            'sqjhc fvjkl (contains soy)',
            'sqjhc mxmxvkd sbzzf (contains fish)',
        ]

    def test_make_food(self):
        self.assertEqual(
            (set(['mxmxvkd', 'kfcds', 'sqjhc', 'nhms']), set(['dairy', 'fish'])),
            make_food(self.lines[0]),
        )

    def test_cant_be_allergen(self):
        self.assertEqual(
            set(['kfcds', 'nhms', 'sbzzf', 'trh']),
            cant_be_allergen([make_food(line) for line in self.lines]),
        )

    def test_part1(self):
        self.assertEqual(5, main(self.lines))

    def test_part2(self):
        self.assertEqual('mxmxvkd,sqjhc,fvjkl', main2(self.lines))
