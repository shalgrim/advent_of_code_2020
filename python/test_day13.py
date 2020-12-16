from unittest import TestCase
from day13_2 import main, does_work, main_attempt_two


class TestDay13(TestCase):
    def test_does_work(self):
        self.assertTrue(does_work(0, 7, 1068781))
        self.assertTrue(does_work(1, 13, 1068781))
        self.assertTrue(does_work(4, 59, 1068781))
        self.assertTrue(does_work(6, 31, 1068781))
        self.assertTrue(does_work(7, 19, 1068781))

    def test_part2(self):
        self.assertEqual(181, main('x,7,3,x,x,x,11,x'))
        self.assertEqual(3417, main('17,x,13,19'))
        self.assertEqual(754018, main('67,7,59,61'))
        self.assertEqual(779210, main('67,x,7,59,61'))
        self.assertEqual(1261476, main('67,7,x,59,61'))
        self.assertEqual(1202161486, main('1789,37,47,1889'))
        self.assertEqual(1068781, main('7,13,x,x,59,x,31,19'))

    def test_part2_version2(self):
        self.assertEqual(181, main_attempt_two('x,7,3,x,x,x,11,x'))
        self.assertEqual(3417, main_attempt_two('17,x,13,19'))
        self.assertEqual(754018, main_attempt_two('67,7,59,61'))
        self.assertEqual(779210, main_attempt_two('67,x,7,59,61'))
        self.assertEqual(1261476, main_attempt_two('67,7,x,59,61'))
        self.assertEqual(1202161486, main_attempt_two('1789,37,47,1889'))
        self.assertEqual(1068781, main_attempt_two('7,13,x,x,59,x,31,19'))
