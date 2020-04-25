import time


def first_turn(frogs, empty_tile_index):
    left_pointer = empty_tile_index - 1
    right_pointer = empty_tile_index + 1

    swap(frogs, left_pointer, empty_tile_index)
    print("".join(frogs))

    empty_tile_index = left_pointer

    swap(frogs, right_pointer, empty_tile_index)
    print("".join(frogs))

    return setting_position(frogs)


def setting_position(frogs):
    empty_tile_index = frogs.index('_')
    right_pointer = empty_tile_index + 1

    while empty_tile_index != 0:
        while check_if_can_move_right_side(frogs):
            swap(frogs, right_pointer, empty_tile_index)
            empty_tile_index = frogs.index('_')
            right_pointer += 1
            print("".join(frogs))

        while check_if_can_move_left_side(frogs):
            if empty_tile_index == 1 and frogs.count('>') % 2 == 0:
                break

            left_pointer = "".join(frogs[:empty_tile_index]).rindex('>')
            swap(frogs, left_pointer, empty_tile_index)
            empty_tile_index = frogs.index('_')
            print("".join(frogs))

    return resolving_position(frogs)


def resolving_position(frogs):
    right_pointer, left_pointer = frogs.index('<'), "".join(frogs).rindex('>')
    empty_tile_index = frogs.index('_')

    while empty_tile_index != len(frogs) // 2:
        while can_resolve_moving_to_the_left(frogs):
            if '<' in frogs[empty_tile_index:]:
                right_pointer = frogs[empty_tile_index:].index('<') + empty_tile_index
            swap(frogs, right_pointer, empty_tile_index)
            empty_tile_index = frogs.index('_')
            print("".join(frogs))

        while can_resolve_moving_to_the_right(frogs):
            if '>' in frogs[:empty_tile_index]:
                left_pointer = "".join(frogs[:empty_tile_index]).rindex('>')
            swap(frogs, left_pointer, empty_tile_index)
            empty_tile_index = frogs.index('_')
            print("".join(frogs))


def can_resolve_moving_to_the_right(frogs):
    frogs_string = "".join(frogs)
    return '><_' in frogs_string or '>_' in frogs_string


def can_resolve_moving_to_the_left(frogs):
    frogs_string = "".join(frogs)
    return '_><' in frogs_string or '_<' in frogs_string


def check_if_can_resolve_position_left_side(frogs):
    frogs_string = "".join(frogs)
    return '>_' in frogs_string or '><_' in frogs_string


def check_if_can_resolve_position_right_side(frogs):
    frogs_string = "".join(frogs)
    return '_<' in frogs_string or '_><' in frogs_string


def check_if_can_move_right_side(frogs):
    frogs_string = "".join(frogs)
    return ('_<' in frogs_string or '_><' in frogs_string) and '<_<' not in frogs_string


def check_if_can_move_left_side(frogs):
    frogs_string = "".join(frogs)
    return ('>_' in frogs_string or '><_' in frogs_string) and '>_>' not in frogs_string


def swap(lst, left, right):
    lst[left], lst[right] = lst[right], lst[left]


def solve(frogs):
    if frogs.count('>') != frogs.count('<') or frogs.count('_') != 1:
        raise ValueError('Wrong swamp')
    first_turn(list(frogs), frogs.index('_'))


def main():
    start_time = time.time()
    solve('>>>_<<<')
    print(time.time() - start_time)


if __name__ == '__main__':
    main()
