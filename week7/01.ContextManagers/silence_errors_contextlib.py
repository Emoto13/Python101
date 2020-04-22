from contextlib import contextmanager


@contextmanager
def silence_errors(exc_type, msg=None):
    try:
        yield
    except exc_type as e:
        if msg is not None and str(e) != msg:
            raise e


def main():
    pass


if __name__ == '__main__':
    main()
