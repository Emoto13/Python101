def iterate(iterable):
    while True:
        for i in iterable:
            yield i


def cycle(iterable):
    for i in iterate(iterable):
        print(i)


def main():
    cycle(range(0, 5))


if __name__ == '__main__':
    main()
