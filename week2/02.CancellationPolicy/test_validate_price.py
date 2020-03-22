import unittest
from cancellation_policy import validate_price


class TestValidatePrice(unittest.TestCase):
    def test_if_validate_price_works_correctly_for_positive_price(self):
        price = 1000
        validate_price(price)

    def test_if_ensure_dates_method_raises_exception_for_negative_price(self):
        price = -1000
        res = None

        try:
            validate_price(price)
        except ValueError as exc:
            res = exc
        self.assertEqual(str(res), 'Price cannot be negative or 0')        
     

    def test_if_validate_price_method_raises_exception_for_price_equal_zero(self):
        price = 0
        res = None

        try:
            validate_price(price)
        except ValueError as exc:
            res = exc
        self.assertEqual(str(res), 'Price cannot be negative or 0')       


if __name__ == '__main__':
    unittest.main()