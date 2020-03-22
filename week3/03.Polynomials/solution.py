import sys
from utils import validate_polynomial, simplify_polynomial


class Polynomial:
    def __init__(self, polynomial):
        validate_polynomial(polynomial)
        polynomial = simplify_polynomial(polynomial)
        self.terms = self.get_all_terms(polynomial)

    def get_all_terms(self, polynomial):
        terms = polynomial.split('+')
        res = self.__parse_terms(terms)
        return res

    # use split
    @staticmethod
    def __parse_terms(terms):
        res = []
        for el in terms:
            if 'x' in el:
                term = None

                if '^' in el:
                    coefficient = el[:el.index('x')]
                    if coefficient != '':
                        term = Term(coefficient=el[:el.index('x')], power=el[el.index('^') + 1:])
                    else:
                        term = Term(power=el[el.index('^') + 1:])
                else:
                    coefficient = el[:el.index('x')]
                    if coefficient != '':
                        term = Term(coefficient=coefficient)
                res.append(str(term))
        return res

    def get_terms(self):
        return self.terms

    def find_derivative(self):
        if not self.terms:
            return '0'
        return "+".join(self.terms)


class Term:
    def __init__(self, coefficient='1', power='1'):
        self.__coefficient = int(coefficient)
        self.__power = int(power)

        self.__upgrade_coefficient()
        self.__lower_power()

    def __str__(self):
        if self.__power == 0:
            return f'{self.__coefficient}'

        if self.__power == 1:
            return f'{self.__coefficient}*x'

        return f'{self.__coefficient}*x^{self.__power}'

    def get_coefficient(self):
        return self.__coefficient

    def get_power(self):
        return self.__power

    def __upgrade_coefficient(self):
        if self.__power > 1:
            self.__coefficient *= self.__power

    def __lower_power(self):
        self.__power -= 1


def main():
    polynomial = sys.argv[1]
    p = Polynomial(polynomial)
    print(p.find_derivative())


if __name__ == '__main__':
    main()
