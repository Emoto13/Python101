import math


def check_if_type_of_argument_is_tuple(fraction):
    if type(fraction) is not tuple:
        raise ValueError('Function argument must be a tuple')


def check_if_denominator_is_zero(fraction):
    denominator = fraction[1]
    if denominator == 0:
        raise ValueError('Denominator cannot be zero')


def validate_fraction(fraction):
    check_if_type_of_argument_is_tuple(fraction)
    check_if_denominator_is_zero(fraction)


def check_if_the_two_numbers_are_equal(nominator, denominator):
    if nominator == denominator:
        return True


def find_simple_fraction(nominator, denominator):
    greatest_common_dividor = math.gcd(nominator, denominator)
    new_n = nominator // greatest_common_dividor
    new_d = denominator // greatest_common_dividor
    return new_n, new_d


def simplify_fractions(fraction):
    validate_fraction(fraction)
    nominator = fraction[0]
    denominator = fraction[1]

    if nominator == 0:
        return 0, 0

    return find_simple_fraction(nominator, denominator)


def main():
    print(simplify_fractions((3, 9)))
    print(simplify_fractions((1, 7)))
    print(simplify_fractions((4, 10)))
    print(simplify_fractions((462, 63)))
    print(simplify_fractions((-8, 4)))
    print(simplify_fractions((0, 4)))


if __name__ == '__main__':
    main()
