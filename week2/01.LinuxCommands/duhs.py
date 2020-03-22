import os
import sys

def convert_bytes(num):
    for x in ['bytes', 'K', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0


def find_file_size(file_path):
    size = os.statvfs(file_path).f_bsize

    return convert_bytes(size)


def main():
    file_path = sys.argv[1]
    print(file_path)
    find_file_size(file_path)


if __name__ == '__main__':
    main()
