import math


class Fraction:
    def __init__(self, nominator, denominator):
        self.__validate_fraction(denominator)

        self.nominator = nominator
        self.denominator = denominator

        self.simplify()

    def __validate_fraction(self, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")

    def __add__(self, other):
        n1 = self.nominator
        n2 = other.nominator

        d1 = self.denominator
        d2 = other.denominator

        new_d = d1 * d2
        n1 *= d2
        n2 *= d1
        new_n = n1 + n2
        return Fraction(new_n, new_d)

    def __eq__(self, other):
        dec1 = self.nominator / self.denominator
        dec2 = other.nominator / other.denominator

        return dec1 == dec2

    def __lt__(self, other):
        dec1 = self.nominator / self.denominator
        dec2 = other.nominator / other.denominator

        return dec1 < dec2

    def __str__(self):
        return f'{self.nominator}/{self.denominator}'

    def __repr__(self):
        return f'Fraction {self.nominator} / {self.denominator}'

    def simplify(self):
        greatest_common_divider = math.gcd(self.nominator, self.denominator)
        self.nominator = self.nominator // greatest_common_divider
        self.denominator = self.denominator // greatest_common_divider

    def convert_to_decimal(self):
        return self.nominator / self.denominator

