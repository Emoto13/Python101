import unittest
from unittest import mock
from datetime import datetime, timedelta
from cancellation_policy import validate_dates


class TestValidateDates(unittest.TestCase):
    def test_if_validate_dates_method_works_correctly(self):
        mock_obj = mock.Mock()
        mock_obj.now = datetime(year=2020, month=4, day=22, hour=10)
        start = mock_obj.now + timedelta(hours=10)
        validate_dates(start, mock_obj.now)

    def test_if_validate_dates_method_raises_exception(self):
        mock_obj = mock.Mock()
        mock_obj.now = datetime(year=2020, month=4, day=22, hour=10)
        start = mock_obj.now + timedelta(hours=-20)

        res = None
        try:
            validate_dates(start, mock_obj.now)
        except ValueError as exc:
            res = exc
        self.assertEqual(str(res), 'Start date cannot be earlier than now')


if __name__ == '__main__':
    unittest.main()
