def accepts(func):
    def execute(*args):
        return func(*args)

    return execute


@accepts
def say_hello(name):
    return f"Hello, I am {name}"


@accepts
def deposit(name, money):
    print(f"{name} sends {money} $!")


def main():
    print(say_hello(4))
    deposit('Marto', 2)


if __name__ == '__main__':
    main()
