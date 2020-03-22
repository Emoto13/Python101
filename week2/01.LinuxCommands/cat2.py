# cat2.py
import sys


def cat2(arguments):
    for argument in arguments:
        with open(argument, 'r') as file:
            print(file.read())


def main():
    cat2(sys.argv[1:len(sys.argv)])

if __name__ == '__main__':
    main()