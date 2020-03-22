import unittest
from solution import TimeUnit

class TestTimeUnitClass(unittest.TestCase):
    def test_if_constructor_sets_values_correctly(self):
        hours = 1
        minutes = 1
        seconds = 1
        tu = TimeUnit(hours=hours, minutes=minutes, seconds=seconds)
        res = hours == tu.hours and minutes == tu.minutes and seconds == tu.seconds
        self.assertTrue(res)

    def test_if_constructor_simplifies_minutes_and_seconds_which_are_over_60_correctly(self):
        hours = 2
        minutes = 2
        seconds = 1
        tu = TimeUnit(hours=1, minutes=61, seconds=61)
        res = hours == tu.hours and minutes == tu.minutes and seconds == tu.seconds
        self.assertTrue(res)

    def test_if_get_seconds_works_correctly(self):
        tu = TimeUnit(hours=1, minutes=1, seconds=1)
        seconds = tu.get_seconds()
        exp = 3661
        self.assertEqual(seconds, exp)

    def test_if_get_minutes_works_correctly(self):
        tu = TimeUnit(hours=1, minutes=1, seconds=1)
        minutes = tu.get_minutes()
        exp = 61
        self.assertEqual(minutes, exp)

    def test_if_get_hours_works_correctly(self):
        tu = TimeUnit(hours=1, minutes=1, seconds=1)
        hours = tu.get_hours()
        exp = 1
        self.assertEqual(hours, exp)

    def test_if_create_time_unit_creates_new_instance_correctly_when_only_minutes_and_seconds_are_given(self):
        tu = TimeUnit.create_time_unit("1:30")
        res = tu.minutes == 1 and tu.seconds == 30
        self.assertTrue(res)

    def test_if_create_time_unit_creates_new_instance_correctly_when_hours_minutes_and_seconds_are_given(self):
        tu = TimeUnit.create_time_unit("1:1:30")
        res = tu.hours == 1 and tu.minutes == 1 and tu.seconds == 30
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
