from types import FunctionType


def required(func):
    def execute(obj):
        name = func.__name__
        subclasses = get_all_subclasses(obj.__class__)
        for subclass in subclasses:
            if name not in get_methods(subclass):
                raise Exception(
                    f'All classes that inherit from "{obj.__class__.__name__}" must provide "{name}" method.')
    return execute


def get_methods(obj):
    return [x for x, y in obj.__dict__.items() if type(y) == FunctionType]


def get_all_subclasses(obj):
    all_subclasses = []

    for subclass in obj.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses


class A:
    def __init__(self):
        pass

    @required
    def a(self):
        print('In a')


class B(A):
    def a(self):
        print("In bн")


def main():
    a = A()
    b = B()
    a.a()


if __name__ == '__main__':
    main()
