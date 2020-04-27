import unittest
from unittest.mock import patch
from cancellation_policy import convert_left_time_to_hours_left
from datetime import datetime, timedelta


class TestConvertToHoursLeftConditions(unittest.TestCase):
    @patch("cancellation_policy.datetime", autospec=True)
    def test_if_convert_left_time_to_hours_left_works_correctly(self, mock_datetime):
        hour_difference = 1

        mock_datetime.now = datetime(year=2020, month=4, day=22, hour=10)
        start = mock_datetime.now + timedelta(hours=hour_difference)
        left_time = start - mock_datetime.now

        hours_left = convert_left_time_to_hours_left(left_time)

        self.assertEqual(hours_left, hour_difference)


if __name__ == '__main__':
    unittest.main()
