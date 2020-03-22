import unittest
from cashdesk import Bill, BatchBill


class TestBatchBillClass(unittest.TestCase):
    def test_if_class_raises_exception_when_init_with_wrong_type_of_argument(self):
        bills = 'a'
        res = None
        try:
            bb = BatchBill(bills)
        except TypeError as e:
            res = str(e)

        self.assertEqual(res, "Type of argument should be list")

    def test_if_class_raises_exception_when_the_bills_is_heterogeneous(self):
        bills = [Bill(i) for i in range(5)]
        bills.append('a')
        res = None
        try:
            bb = BatchBill(bills)
        except ValueError as e:
            res = str(e)

        self.assertEqual(res, "BatchBill should only contain Bills")

    def test_if_init_of_class_works_with_empty_list(self):
        bills = []
        bb = BatchBill(bills)

    def test_if___getitem____dunder_works_correctly(self):
        bills = [Bill(i) for i in range(5)]
        bb = BatchBill(bills)
        b = Bill(1)
        self.assertEqual(b, bb[1])

    def test_if___len____dunder_works_correctly(self):
        bills = [Bill(i) for i in range(5)]
        bb = BatchBill(bills)
        res = 5
        self.assertEqual(res, len(bb))

    def test_if_total_works_correctly(self):
        bills = [Bill(i) for i in range(5)]
        bb = BatchBill(bills)
        res = 10
        self.assertEqual(res, bb.total())

    def test_if_append_works_correctly(self):
        bb = BatchBill()
        b = Bill(1)
        bb.append(b)

        self.assertEqual(1, len(bb))

    def test_if_append_raises_exception_when_argument_is_not_a_bill(self):
        bb = BatchBill()
        res = None
        try:
            bb.append('a')
        except TypeError as e:
            res = str(e)

        self.assertEqual(res, 'BatchBill can only append Bill')


if __name__ == '__main__':
    unittest.main()
