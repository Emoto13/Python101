def go_deeper(data, current_key, key, value):
    if current_key == key:
        data[current_key] = value

    if type(data[current_key]) is dict:
        find_value(data[current_key], key, value)

    if type(data[current_key]) is list or type(data[current_key]) is tuple:
        for element in data[current_key]:
            if type(element) is dict:
                find_value(element, key, value)


def check_if_there_is_an_answer(res):
    return res is not None


def find_value(data, key, value):
    for k in data:
        go_deeper(data, k, key, value)


def deep_update(data, key, value):
    find_value(data, key, value)
    print(data)


def main():
    deep_update(
        {'v': 7,
         'a':
             {'b': [1, 2, 4, 2,
                    {'d': [
                        {
                            'c': 3
                        }]
                    },
                    {'c': 42}]
              },
         'c': 8
         }, 'c', 0)

    dicts1 = {'a': ['a', 2, 4, 2],
              'b': {'foo': {'bar'}}}

    dicts2 = ['a', 2, 4, 2]

    print(dicts1 == dicts2)


if __name__ == '__main__':
    main()
