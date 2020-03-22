from simplify_fractions import simplify_fractions


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


def find_common_denominator(denominators):
    current_common_denominator = denominators[0]

    for i in range(1, len(denominators)):
        current_denominator = denominators[i]

        if not (current_common_denominator / current_denominator).is_integer():
            if (current_denominator / current_common_denominator).is_integer():
                current_common_denominator = current_denominator
                continue
            current_common_denominator *= current_denominator
    return current_common_denominator


def expand_fractions(fractions, common_denominator):
    new_fractions = []
    for fraction in fractions:
        nominator = fraction[0]
        denominator = fraction[1]

        difference_between_a_and_cd = int(common_denominator / denominator)
        new_nominator = nominator * difference_between_a_and_cd
        new_fractions.append((new_nominator, common_denominator))

    return new_fractions


def sum_fractions(fractions):
    nominator = sum([fraction[0] for fraction in fractions])
    denominator = fractions[0][1]
    res_fraction = simplify_fractions((nominator, denominator))
    return res_fraction


def collect_fractions(fractions):
    validate_input(fractions)

    denominators = [fraction[1] for fraction in fractions]

    common_denominator = find_common_denominator(denominators)
    fractions = expand_fractions(fractions, common_denominator)

    res = sum_fractions(fractions)
    return res


def main():
    print(collect_fractions([(1, 2), (3, 2)]))


if __name__ == '__main__':
    main()
