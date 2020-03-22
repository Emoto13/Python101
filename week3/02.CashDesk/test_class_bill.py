import unittest
from cashdesk import Bill


class TestBillClass(unittest.TestCase):
    def test_if_class_raises_exception_when_the_amount_is_not_an_integer(self):
        res = None
        try:
            bill = Bill('a')
        except TypeError as e:
            res = str(e)

        self.assertEqual(res, 'Amount should be an integer')

    def test_if_class_raises_exception_when_the_amount_is_negative(self):
        res = None
        try:
            bill = Bill(-10)
        except ValueError as e:
            res = str(e)

        self.assertEqual(res, 'The amount cannot be below zero')

    def test_if___repr___dunder_works_correctly(self):
        b = Bill(1)
        res = 'A 1$ bill'

        self.assertEqual(res, repr(b))

    def test_if___str___dunder_works_correctly(self):
        b = Bill(1)
        res = 'A 1$ bill'

        self.assertEqual(res, str(b))

    def test_if___int___dunder_works_correctly(self):
        b = Bill(1)
        res = 1

        self.assertEqual(res, int(b))

    def test_if___eq___dunder_works_correctly(self):
        b1 = Bill(1)
        b2 = Bill(2)
        b3 = Bill(1)

        self.assertFalse(b1 == b2)
        self.assertTrue(b1 == b3)

    def test_if___hash___dunder_works_correctly(self):
        b = Bill(1)
        res = 1

        self.assertEqual(res, hash(b))

if __name__ == '__main__':
    unittest.main()
