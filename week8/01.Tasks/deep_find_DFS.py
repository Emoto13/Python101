def go_deeper(data, current_key, key):
    if current_key == key:
        return data[key]

    if type(data[current_key]) is dict:
        res = find_value(data[current_key], key)
        if check_if_there_is_an_answer(res):
            return res

    if type(data[current_key]) is list or type(data[current_key]) is tuple:
        for element in data[current_key]:
            if type(element) is dict:
                res = find_value(element, key)
                if check_if_there_is_an_answer(res):
                    return res


def check_if_there_is_an_answer(res):
    return res is not None


def find_value(data, key):
    for k in data:
        res = go_deeper(data, k, key)
        if check_if_there_is_an_answer(res):
            return res


def deep_find(data, key):
    print(find_value(data, key))


def main():
    deep_find(
        {'v': 7,
         'a':
             {'b': [1, 2, {'a': 9}, 4, 2,
                    {'d': [
                        {
                            'f': 9
                        },
                        {
                            'c': 9
                        }]
                    }]
              },
         'c' : 4
         }, 'c')


if __name__ == '__main__':
    main()
