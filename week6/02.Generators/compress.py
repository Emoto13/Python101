def iterate(iterable, mask):
    mx = min(len(iterable), len(mask))

    for i in range(mx):
        if mask[i]:
            yield iterable[i]


def compress_functional(iterable, mask):
    res = list(map(lambda x: x[0], filter(lambda x: x[1], zip(iterable, mask))))
    return res


def compress(iterable, mask):
    return [i for i in iterate(iterable, mask)]


def main():
    print(compress_functional(['Ivan', 'Gosho', 'Panda'], [False, False, True]))


if __name__ == '__main__':
    main()
