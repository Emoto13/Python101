def gas_stations(distance, tank_size, stations):
    n = len(stations)
    passed_distance = 0
    current_gas = tank_size
    res_list = []

    for i in range(0, n):
        if passed_distance >= distance:
            break

        prev_station = 0
        current_station = stations[i]

        if i != 0:
            prev_station = stations[i - 1]

        current_gas -= (current_station - prev_station)
        passed_distance = stations[i]

        if i == n - 1:
            remaining_distance = distance - stations[i]
            if current_gas < remaining_distance:
                current_gas = tank_size
                res_list.append(stations[i])

        if i != n - 1 and current_gas < stations[i + 1] - stations[i]:
            current_gas = tank_size
            res_list.append(stations[i])

    return res_list


print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))


def is_number_balanced(number):
    stringified_number = str(number)
    n = len(stringified_number)
    first_half = 0
    second_half = 0
    if n % 2 == 0:
        first_half = stringified_number[0:n // 2]
        second_half = stringified_number[n // 2:n]
    else:
        first_half = stringified_number[0:n // 2]
        second_half = stringified_number[n // 2 + 1:n]

    first_number = sum([int(i) for i in first_half])
    second_number = sum([int(i) for i in second_half])

    if first_number == second_number:
        return True
    else:
        return False


print(is_number_balanced(123123))
print(is_number_balanced(1231123))
print(is_number_balanced(123456))


def increasing_or_decreasing(seq):
    is_increasing = seq[0] < seq[1]

    for i in range(1, len(seq)):
        current = seq[i]
        prev = seq[i - 1]
        if is_increasing and current <= prev:
            return False

        if not is_increasing and current >= prev:
            return False

    if is_increasing:
        return 'Up!'
    else:
        return 'Down!'


print(increasing_or_decreasing([1, 2, 3, 4, 5]))
print(increasing_or_decreasing([5, 6, -10]))
print(increasing_or_decreasing([1, 1, 1, 1]))
print(increasing_or_decreasing([9, 8, 7, 6]))


def palindrome(object):
    reverseInput = "".join(reversed(str(object)))
    return str(object) == reverseInput


def get_largest_palindrome(n):
    for i in reversed(range(n)):
        if palindrome(i):
            return i


print(get_largest_palindrome(100))


def sum_of_numbers(input_string):
    current_digits = []
    total = 0
    lst_input_string = list(input_string)

    for i in range(0, len(lst_input_string)):
        current_num = lst_input_string[i]
        if current_num.isdigit():
            for j in range(i, len(input_string)):
                current_num = lst_input_string[j]

                if current_num.isdigit():
                    current_digits.append(current_num)
                    lst_input_string[j] = '-'

                else:
                    total += int(''.join(current_digits))
                    current_digits.clear()
                    break

    if current_digits:
        total += int(''.join(current_digits))

    return total


print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
print(sum_of_numbers("1101"))
print(sum_of_numbers("1111O"))
print(sum_of_numbers("1abc33xyz22"))
print(sum_of_numbers("0hfabnek"))


def birthday_ranges(birthdays, ranges):
    date_and_number_of_birthdays = {birthdays[i]: birthdays.count(birthdays[i]) for i in range(len(birthdays))}
    res_list = []

    for current_range in ranges:
        start = current_range[0]
        end = current_range[1] + 1
        birthdays_in_range = 0

        for i in range(start, end):
            if i not in date_and_number_of_birthdays.keys():
                date_and_number_of_birthdays[i] = 0
            birthdays_in_range += date_and_number_of_birthdays[i]

        res_list.append(birthdays_in_range)

    return res_list


print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))


def group(lst):
    n = len(lst)
    new_list = [str(lst[0])]
    res_list = []

    for i in range(1, n):
        if lst[i] != lst[i - 1]:
            res_list.append(new_list.copy())
            new_list.clear()

        new_list.append(str(lst[i]))

    if new_list:
        res_list.append(new_list)

    return res_list


def numbers_to_message(pressed_sequence):
    dictionary = {
        '2': 'a',
        '22': 'b',
        '222': 'c',
        '3': 'd',
        '33': 'e',
        '333': 'f',
        '4': 'g',
        '44': 'h',
        '444': 'i',
        '5': 'j',
        '55': 'k',
        '555': 'l',
        '6': 'm',
        '66': 'n',
        '666': 'o',
        '7': 'p',
        '77': 'q',
        '777': 'r',
        '7777': 's',
        '8': 't',
        '88': 'u',
        '888': 'v',
        '9': 'w',
        '99': 'x',
        '999': 'x',
        '9999': 'z',
        '0': ' ',
    }

    message_list = []
    capitalize = False
    res_list = []
    grouped = group(pressed_sequence)

    for current_group in grouped:
        if current_group == ['1']:
            capitalize = True
            continue

        if current_group == ['-1']:
            continue

        length = len(current_group)
        string_group = ''.join(current_group)

        if length > 4 and '7777' in string_group or '9999' in string_group:
            length = length % 4
            string_group = string_group[0:length]

        if length >= 4 and '7777' not in string_group or '9999' not in string_group:
            length = length % 3
            if length == 0:
                length = 3
            string_group = string_group[0:length]

        if capitalize == True:
            res_list.append(dictionary[string_group].upper())
            capitalize = False
            continue

        res_list.append(dictionary[string_group])

    return ''.join(res_list)


print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
print(numbers_to_message([2, 2, 2, 2]))
print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def message_to_numbers(message):
    dictionary = {
        '2': 'a',
        '22': 'b',
        '222': 'c',
        '3': 'd',
        '33': 'e',
        '333': 'f',
        '4': 'g',
        '44': 'h',
        '444': 'i',
        '5': 'j',
        '55': 'k',
        '555': 'l',
        '6': 'm',
        '66': 'n',
        '666': 'o',
        '7': 'p',
        '77': 'q',
        '777': 'r',
        '7777': 's',
        '8': 't',
        '88': 'u',
        '888': 'v',
        '9': 'w',
        '99': 'x',
        '999': 'y',
        '9999': 'z',
        '0': ' ',

        '12': 'A',
        '122': 'B',
        '1222': 'C',
        '13': 'D',
        '133': 'E',
        '1333': 'F',
        '14': 'G',
        '144': 'H',
        '1444': 'I',
        '15': 'J',
        '155': 'K',
        '1555': 'L',
        '16': 'M',
        '166': 'N',
        '1666': 'O',
        '17': 'P',
        '177': 'Q',
        '1777': 'R',
        '17777': 'S',
        '18': 'T',
        '188': 'U',
        '1888': 'V',
        '19': 'W',
        '199': 'X',
        '1999': 'Y',
        '19999': 'Z',
    }

    reverse_dictionary = {value: list(map(int, key)) for key, value in dictionary.items()}
    res_list = []
    for i in range(len(message)):
        current_message = message[i]
        first_letter = current_message[0]

        if i > 0 and reverse_dictionary[current_message][0] == reverse_dictionary[message[i - 1]][0]:
            res_list.append(-1)

        res_list.extend(reverse_dictionary[current_message])
    return res_list


print(message_to_numbers("abc"))
print(message_to_numbers("a"))
print(message_to_numbers("Ivo e Panda"))
print(message_to_numbers("aabbcc"))
