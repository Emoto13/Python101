# generate_numbers.py
import sys
from random import randint


def generate_numbers(filename, numbers):
    str_numbers = " ".join(numbers)
    with open(filename, 'w') as f:
        f.write(str_numbers)


def main():
    integers_to_write = int(sys.argv[2])
    numbers = [str(randint(1, 1000)) for i in range(integers_to_write)]

    filename = sys.argv[1]
    generate_numbers(filename, numbers)


if __name__ == '__main__':
    main()
