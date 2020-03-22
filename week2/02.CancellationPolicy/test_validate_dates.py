import unittest
from datetime import datetime, timedelta
from cancellation_policy import validate_dates


class TestValidateDates(unittest.TestCase):
    def test_if_validate_dates_method_works_correctly(self):
        now = datetime.now()
        start = now + timedelta(hours = 10)
        validate_dates(start, now)

    def test_if_validate_dates_method_raises_exception(self):
        now = datetime.now()
        start = now + timedelta(hours = -20)

        res = None
        try:
            validate_dates(start, now)
        except ValueError as exc:
            res = exc
        self.assertEqual(str(res), 'Start date cannot be earlier than now')        
           


if __name__ == '__main__':
    unittest.main()