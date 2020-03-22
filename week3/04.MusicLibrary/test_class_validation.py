import unittest
from validation import Validation


class TestValidationClass(unittest.TestCase):
    def test_if_validate_that_arguments_are_not_empty_strings_raises_exception(self):
        title = ""
        artist = ""
        album = ""
        length = ""
        res = None
        exp = "Arguments cannot missed or be empty strings"
        try:
            Validation.validate_that_arguments_are_not_empty_strings(title, artist, album, length)
        except Exception as e:
            res = str(e)

        self.assertEqual(res, exp)

    def test_if_validate_that_arguments_are_not_empty_strings_works_correctly_for_valid_arguments(self):
        title = "A"
        artist = "B"
        album = "C"
        length = "1:30"
        res = None
        exp = "Arguments cannot missed or be empty strings"
        Validation.validate_that_arguments_are_not_empty_strings(title, artist, album, length)

    def test_if_validate_length_raises_exception_for_wrong_format_of_length(self):
        length1 = "1-12-1"
        length2 = ":44"

        res1 = None
        res2 = None
        exp = "Length should be in format 'hh:mm:ss'"
        try:
            Validation.validate_length(length1)
        except Exception as e:
            res1 = str(e)

        try:
            Validation.validate_length(length2)
        except Exception as e:
            res2 = str(e)

        self.assertEqual(res1, exp)
        self.assertEqual(res2, exp)

    def test_if_validate_length_works_correctly_for_valid_length(self):
        length = "1:30"
        Validation.validate_length(length)


if __name__ == '__main__':
    unittest.main()
