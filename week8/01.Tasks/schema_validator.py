def get_all_dicts_keys(dicts):
    iterate_dict(dicts)


def iterate_dict(dicts):
    for key in dicts:
        dicts_keys.append(key)
        if type(dicts[key]) is dict:
            iterate_dict(dicts[key])


def get_all_list_keys(lst):
    iterate_list(lst)


def iterate_list(lst):
    for el in lst:
        if type(el) is list:
            iterate_list(el)
        else:
            list_keys.append(el)


def schema_validator(lst, dicts):
    global list_keys
    list_keys = []
    get_all_list_keys(lst)

    global dicts_keys
    dicts_keys = []
    get_all_dicts_keys(dicts)

    return list_keys == dicts_keys


def main():
    print(schema_validator([
        'key1',
        'key2',
        [
            'key3',
            ['inner_key1', 'inner_key2'],
        ]
    ], {
        'key1': 'val1',
        'key2': 'val2',
        'key3': {
            'inner_key1': 'val1',
            'inner_key2': 'val2'
        }
    }))


if __name__ == '__main__':
    main()
