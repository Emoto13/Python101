import unittest
from collect_fractions import sum_fractions


class TestSumFractions(unittest.TestCase):
    def test_sum_fractions_when_no_simplifying_is_needed(self):
        fractions = [(4, 4), (2, 4), (1, 4)]
        res = sum_fractions(fractions)
        exp = (7, 4)
        self.assertEqual(res, exp)

    def test_sum_when_simplifying_is_needed(self):
        fractions = [(5, 4), (2, 4), (1, 4)]
        res = sum_fractions(fractions)
        exp = (2, 1)
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
