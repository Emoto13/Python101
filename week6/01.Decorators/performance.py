from datetime import datetime
from time import sleep


def performance(path):
    def execute(func):
        start_time = datetime.now()

        def inner():
            func()
            with open(path, 'a') as file:
                file.write(f'{func.__name__} was called and took  '
                           f'{(datetime.now() - start_time).total_seconds()} seconds\n')

        return inner

    return execute


@performance('log.txt')
def something_heavy():
    sleep(2)
    return "I am done!"


def main():
    something_heavy()


if __name__ == '__main__':
    main()
