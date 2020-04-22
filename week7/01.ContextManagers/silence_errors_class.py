class silence_errors:
    def __init__(self, exc_type, msg=None):
        self.exc_type = exc_type
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value):
        same_exception_type = self.exc_type == exc_type
        correct_message = self.msg is None or str(exc_value) == self.msg

        return same_exception_type and correct_message


def main():
    pass


if __name__ == '__main__':
    main()
