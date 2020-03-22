def bubble_sort(arr, key):
    if key is '':
        return bubble_sort_for_simple_objects(arr)
    else:
        return bubble_sort_for_dictionaries(arr, key)


def bubble_sort_for_simple_objects(arr):
    n = len(arr)
    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_for_dictionaries(arr, key):
    n = len(arr)
    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def change_order_based_on_ascending(cast_arr, ascending):
    if not ascending and type(cast_arr) is tuple:
        return tuple(reversed(cast_arr))
    elif not ascending:
        return list(reversed(cast_arr))
    return cast_arr


def validate_that_arr_is_homogeneous(arr):
    current_type = None
    for i in arr:
        if current_type is not None and type(i) != current_type:
            raise ValueError('Cannot sort array which contains different types of elements')
        current_type = type(i)


def validate_dict_arr(arr, key):
    is_list_of_dictionaries = False
    for i in arr:
        if type(i) is dict:
            is_list_of_dictionaries = True

    if is_list_of_dictionaries and key == '':
        raise ValueError('Cannot sort array of dictionaries without a given key')


def validate_arr_data(arr, key):
    validate_that_arr_is_homogeneous(arr)
    validate_dict_arr(arr, key)


def python_sort(arr=None, ascending=True, key=''):
    if arr is None:
        arr = []

    cast_arr = None

    validate_arr_data(arr, key)

    if type(arr) is tuple:
        cast_arr = list(arr)
        cast_arr = tuple(bubble_sort(cast_arr, key))
    else:
        cast_arr = bubble_sort(arr, key)

    cast_arr = change_order_based_on_ascending(cast_arr, ascending)

    return cast_arr


def main():
    pass


if __name__ == '__main__':
    main()
