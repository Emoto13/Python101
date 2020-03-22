# cat.py
import sys

def cat(arguments):
    with open(arguments, 'r') as f:
        print(f.read())

def main():
    cat(sys.argv[1])


if __name__ == '__main__':
    main()
