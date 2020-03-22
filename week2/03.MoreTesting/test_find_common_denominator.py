import unittest
from collect_fractions import find_common_denominator

class TestFindCommonDenominator(unittest.TestCase):
    def test_find_common_denominator_when_denominators_are_product_of_each_other(self):
        denominators = [1, 2 ,4]
        res = find_common_denominator(denominators)
        self.assertEqual(res, 4)

    def test_find_common_denominator_when_denominators_are_all_different(self):
        denominators = [1, 2, 3, 5]
        res = find_common_denominator(denominators)
        self.assertEqual(res, 30)
    


if __name__ == '__main__':
    unittest.main()
