from unittest import TestCase

from day17_1 import count_active_cubes, active_cubes_from_lines, get_active_cubes
from day17_2 import count_active_cubes_4d, active_cubes_from_lines_4d


class TestDay17(TestCase):
    def test_get_active_cubes(self):
        lines = ['.#.', '..#', '###']
        active_cubes = active_cubes_from_lines(lines)
        self.assertEqual(
            set(
                [
                    (0, 1, -1),
                    (2, 2, -1),
                    (1, 3, -1),
                    (0, 1, 0),
                    (2, 1, 0),
                    (1, 2, 0),
                    (2, 2, 0),
                    (1, 3, 0),
                    (0, 1, 1),
                    (2, 2, 1),
                    (1, 3, 1),
                ]
            ),
            get_active_cubes(active_cubes, 1),
        )

    def test_part1(self):
        lines = ['.#.', '..#', '###']
        active_cubes = active_cubes_from_lines(lines)
        self.assertEqual(11, count_active_cubes(active_cubes, 1))
        active_cubes = active_cubes_from_lines(lines)
        self.assertEqual(21, count_active_cubes(active_cubes, 2))
        active_cubes = active_cubes_from_lines(lines)
        self.assertEqual(112, count_active_cubes(active_cubes, 6))

    def test_part2(self):
        lines = ['.#.', '..#', '###']
        active_cubes = active_cubes_from_lines_4d(lines)
        self.assertEqual(848, count_active_cubes_4d(active_cubes, 6))
