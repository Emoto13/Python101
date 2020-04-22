from decimal import *
from contextlib import contextmanager


@contextmanager
def change_precision(precision):
    try:
        getcontext().prec = precision
        yield precision
    except Exception as e:
        return type(e) and str(e)


def main():
    with change_precision(5):
        print(Decimal(2.4114212) + Decimal(1.42324))


if __name__ == '__main__':
    main()
