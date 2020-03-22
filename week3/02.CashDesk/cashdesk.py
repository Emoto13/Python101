class Bill:
    def __init__(self, amount):
        self.__validate_amount(amount)
        self.__amount = amount

    @staticmethod
    def __validate_amount(amount):
        if type(amount) is not int:
            raise TypeError('Amount should be an integer')
        if amount < 0:
            raise ValueError('The amount cannot be below zero')

    def __repr__(self):
        return f'A {self.__amount}$ bill'

    def __str__(self):
        return f'A {self.__amount}$ bill'

    def __int__(self):
        return self.__amount

    def __eq__(self, other):
        return self.__amount == int(other)

    def __hash__(self):
        return self.__amount


class BatchBill:
    def __init__(self, bills=None):
        if bills is None:
            bills = []
        self.__validate_bills(bills)
        self.__bills = bills
        self.__total_of_bills = self.__get_total(bills)

    @staticmethod
    def __get_total(bills):
        total = 0
        for bill in bills:
            total += int(bill)
        return total

    @staticmethod
    def __check_if_bills_contain_only_objects_of_type_bill(bills):
        contains_only_bills = True
        for bill in bills:
            if type(bill) is not Bill:
                contains_only_bills = False
                break
        return contains_only_bills

    def __validate_bills(self, bills):
        if type(bills) is not list:
            raise TypeError("Type of argument should be list")

        if not self.__check_if_bills_contain_only_objects_of_type_bill(bills):
            raise ValueError("BatchBill should only contain Bills")

    def __getitem__(self, index):
        return self.__bills[index]

    def __len__(self):
        return len(self.__bills)

    def total(self):
        return self.__total_of_bills

    def append(self, bill):
        if type(bill) is not Bill:
            raise TypeError('BatchBill can only append Bill')
        self.__bills.append(bill)
        self.__total_of_bills += int(bill)


class CashDesk:
    def __init__(self):
        self.__dict = {}
        self.__total_money = 0

    def __handle_if_case_bill(self, money):
        if str(money) not in self.__dict:
            self.__dict[str(money)] = 0
        self.__dict[str(money)] += 1
        self.__total_money += int(money)

    def __handle_if_case_batch(self, money):
        for bill in money:
            if str(bill) not in self.__dict:
                self.__dict[str(bill)] = 0
            self.__dict[str(bill)] += 1
            self.__total_money += int(bill)

    def take_money(self, money):
        if type(money) is Bill:
            self.__handle_if_case_bill(money)
        elif type(money) is BatchBill:
            self.__handle_if_case_batch(money)
        else:
            raise TypeError('Function accepts only objects of type Bill or BatchBill')

    def stringify(self):
        lst = []
        keys = sorted(list(self.__dict.keys()))
        for key in keys:
            lst.append(f'{key} - {self.__dict[key]}\n')
        return "".join(lst).strip()

    def inspect(self):
        print(self.stringify())

    def total(self):
        return self.__total_money
