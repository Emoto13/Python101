def silence(path):
    def execute(func):
        def inner(*args):
            try:
                func(*args)
            except Exception as e:
                with open(path, 'a') as f:
                    f.write(str(e))
                    f.write('\n')

        return inner
    return execute


@silence('silence.txt')
def foo(x):
    if x > 50:
        raise ValueError('Omg.')


def main():
    foo(100)


if __name__ == '__main__':
    main()
