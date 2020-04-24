def deep_find(data, key):
    queue = []

    for k, v in data.items():
        queue.append((k, v))

    while queue:
        element = queue.pop(0)
        element_key = element[0]
        element_value = element[1]

        if type(element_key) == type(key) and element_key == key:
            return element[1]

        if type(element_value) is tuple or type(element_value) is list:
            for el in element_value:
                if type(el) is dict:
                    for k, v in el.items():
                        queue.append((k, v))

        if type(element_value) is dict:
            for k, v in element_value.items():
                queue.append((k, v))


def main():
    print(deep_find(
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
         'c': 4
         }, 'c'))


if __name__ == '__main__':
    main()
