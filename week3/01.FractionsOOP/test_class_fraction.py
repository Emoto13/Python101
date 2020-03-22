import unittest
from fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_if_class_raises_exception_if_denominator_is_zero(self):
        res = None
        try:
            f = Fraction(10, 0)
        except ValueError as e:
            res = str(e)

        self.assertIsNotNone(res, "Fraction class didn't raise exception when denominator was 0")

    def test_if_class_works_correctly_if_(self):
        res = None
        f = Fraction(10, 1)

        self.assertIsNone(res)

    def test_if____str____dunder_works_correctly(self):
        f1 = Fraction(1, 3)
        f2 = Fraction(2, 4)

        self.assertEqual("1/3", str(f1))
        self.assertEqual("1/2", str(f2))

    def test_if____repr____dunder_works_correctly(self):
        f1 = Fraction(1, 3)
        f2 = Fraction(2, 4)

        self.assertEqual('Fraction 1 / 3', repr(f1))
        self.assertEqual('Fraction 1 / 2', repr(f2))

    def test_if___add___dunder_works_correctly(self):
        f1 = Fraction(1, 3)  # 2 ,6
        f2 = Fraction(2, 4)  # 3 , 6

        f3 = f1 + f2
        f4 = f1 + f2 + f3

        self.assertEqual('Fraction 5 / 6', repr(f3))
        self.assertEqual('Fraction 5 / 3', repr(f4))

    def test_if_convert_to_decimal_works_correctly(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)

        dec1 = f1.convert_to_decimal()
        dec2 = f2.convert_to_decimal()
        self.assertEqual(dec1, 0.5)
        self.assertEqual(dec2, 0.3333333333333333)

    def test_if___eq___dunder_work_correctly(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 5)

        f3 = Fraction(1, 2)
        f4 = Fraction(2, 4)

        res_of_equation_false = f1 == f2
        res_of_equation_true = f3 == f4

        self.assertFalse(res_of_equation_false)
        self.assertTrue(res_of_equation_true)

    def test_if___lt___dunder_work_correctly(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 5)

        res_of_equation_false = f1 > f2
        res_of_equation_true = f1 < f2

        self.assertEqual(res_of_equation_false, False)
        self.assertEqual(res_of_equation_true, True)


if __name__ == '__main__':
    unittest.main()
