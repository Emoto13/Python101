def iterate(iterable):
    for i in iterable:
        yield i


def create_list(iterable):
    res = []
    iterator = iterate(iterable)
    for j in range(2):
        for i in iterator:
            res.append(i)
        iterable = yield res
        iterator = iterate(iterable)


def chain(iter1, iter2):
    gen = create_list(iter1)
    next(gen)
    return list(gen.send(iter2))


def main():
    print(chain(range(0, 4), range(4, 8)))


if __name__ == '__main__':
    main()
