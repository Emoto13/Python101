def ensure_input_is_a_list(fractions):
    if type(fractions) is not list:
        raise ValueError('Input must be a list of tuples')


def ensure_input_is_not_an_empty_list(fractions):
    if not fractions:
        raise ValueError('Input cannot be an empty list')


def ensure_input_is_a_homogeneous_list(fractions):
    for fraction in fractions:
        if type(fraction) is not tuple:
            raise ValueError('Input must only consist of fractions(tuples)')


def ensure_input_doesnt_contain_denominator_with_zero(fractions):
    for fraction in fractions:
        if fraction[1] == 0:
            raise ValueError('Fraction with 0 as denominator')


def validate_input(fractions):
    ensure_input_is_a_list(fractions)
    ensure_input_is_not_an_empty_list(fractions)
    ensure_input_is_a_homogeneous_list(fractions)
    ensure_input_doesnt_contain_denominator_with_zero(fractions)


def check_order_by_ascending(fractions, ascending):
    if not ascending:
        return list(reversed(fractions))
    return fractions


def sort_fractions(fractions, ascending=True):
    validate_input(fractions)
    arr_of_decimals = [(fraction[0] / fraction[1]) for fraction in fractions]
    dictionary = {arr_of_decimals[i]: fractions[i] for i in range(len(fractions))}
    arr_of_decimals.sort()
    fractions = [dictionary[el] for el in arr_of_decimals]

    fractions = check_order_by_ascending(fractions, ascending)

    return fractions


def main():
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)], ascending=False))


if __name__ == '__main__':
    main()
