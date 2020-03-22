import unittest
from cashdesk import Bill, BatchBill, CashDesk


class TestBatchBillClass(unittest.TestCase):
    def test_if_take_money_works_with_bill(self):
        bill = Bill(10)
        cd = CashDesk()
        cd.take_money(bill)
        res = 10

        self.assertEqual(res, cd.total())

    def test_if_take_money_works_with_batch(self):
        bills = [Bill(i) for i in range(5)]
        batch = BatchBill(bills)
        cd = CashDesk()
        cd.take_money(batch)
        res = 10

        self.assertEqual(res, cd.total())

    def test_if_take_money_raises_exception_when_argument_is_not_of_type_bill_nor_batch(self):
        cd = CashDesk()
        res = None
        try:
            cd.take_money('a')
        except TypeError as e:
            res = str(e)
        self.assertEqual(res, 'Function accepts only objects of type Bill or BatchBill')

    def test_if___stringify_works_correctly(self):
        bills = [Bill(i) for i in range(5)]
        batch = BatchBill(bills)
        cd = CashDesk()
        cd.take_money(batch)
        cd.take_money(Bill(1))
        s = cd.stringify()

        self.assertEqual(s, "A 0$ bill - 1\nA 1$ bill - 2\nA 2$ bill - 1\nA 3$ bill - 1\nA 4$ bill - 1")



if __name__ == '__main__':
    unittest.main()
