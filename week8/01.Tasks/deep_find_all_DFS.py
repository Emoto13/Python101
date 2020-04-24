def go_deeper(data, current_key, key):
    if current_key == key:
        res.append(data[key])

    if type(data[current_key]) is dict:
        iterate_dict(data[current_key], key)

    if type(data[current_key]) is list or type(data[current_key]) is tuple:
        for element in data[current_key]:
            if type(element) is dict:
                iterate_dict(element, key)


def iterate_dict(dicts, key):
    for k in dicts:
        go_deeper(dicts, k, key)


def find_values(data, key):
    global res
    res = []

    iterate_dict(data, key)
    return res


def deep_find_all(data, key):
    print(find_values(data, key))


def main():
    deep_find_all(
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
         }, 'c')


if __name__ == '__main__':
    main()
