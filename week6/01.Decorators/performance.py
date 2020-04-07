from datetime import datetime
from time import sleep


def performance(func):
    def execute(path):
        return func(path)
    return execute


@performance
def something_heavy(path):
    start_time = datetime.now()
    sleep(2)
    with open(path, 'a') as f:
        f.write(f'{something_heavy.__name__} was called and took '
                f'{(datetime.now() - start_time).total_seconds()} seconds\n')
    return "I am done!"


def main():
    something_heavy('log.txt')
    something_heavy('log.txt')
    something_heavy('log.txt')
    something_heavy('log.txt')


if __name__ == '__main__':
    main()
