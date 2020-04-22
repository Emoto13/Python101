from decimal import *


class change_precision:
    def __init__(self, precision):
        self.precision = precision

    def __enter__(self):
        getcontext().prec = self.precision
        return self.precision

    def __exit__(self, exc_type, exc_value, exc_tb):
        return exc_type and exc_value


def main():
    with change_precision(5):
        print(Decimal(2.4114212) + Decimal(1.42324))


if __name__ == '__main__':
    main()
