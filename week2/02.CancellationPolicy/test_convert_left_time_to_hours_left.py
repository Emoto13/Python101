import unittest
from cancellation_policy import convert_left_time_to_hours_left
from datetime import datetime, timedelta

class TestConvertToHoursLeftConditions(unittest.TestCase):
    def test_if_convert_left_time_to_hours_left_works_correctly(self):
        hour_difference = 1

        now = datetime.now() 
        start = now + timedelta(hours=hour_difference)
        left_time = start - now


        hours_left = convert_left_time_to_hours_left(left_time)


        self.assertEqual(hours_left, hour_difference)






if __name__ == '__main__':
    unittest.main()