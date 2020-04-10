from read_input import get_key_input
from os import path


def get_page_number(current_page):
    if current_page < 10:
        return f'00{current_page}'

    if current_page < 100:
        return f'0{current_page}'

    return f'{current_page}'


def check_if_path_exists(file_path):
    return path.exists(file_path)


def check_if_key_is_valid(key):
    if key != ' ':
        print('Wrong key. Try again')
        return False
    return True


def get_page(current_page):
    page_number = get_page_number(current_page)
    file_path = f'book/{page_number}.txt'

    with open(file_path, 'r') as file:
        return file.read()


def concatenate_pages():
    current_page = 1
    page_number = get_page_number(current_page)

    book = ""
    while check_if_path_exists(f'book/{page_number}.txt'):
        with open(f'book/{page_number}.txt', 'r') as f:
            book += f.read()
            book += '\n'
            current_page += 1
            page_number = get_page_number(current_page)
    return book


def create_book():
    book = concatenate_pages()

    with open(f'book/book.txt', 'w') as f:
        f.write(book)


def iterate(book_path):
    with open(f'{book_path}', 'r') as f:
        text = ""
        for line in f:
            if '# Chapter' in line:
                yield text
                text = ''

            text += line
        yield text
        return


def book_reader(book_path=""):
    if book_path == "":
        create_book()
        book_path = 'book/book.txt'
    gen = iterate(book_path)

    for i in gen:
        key = get_key_input()
        while not check_if_key_is_valid(key):
            key = get_key_input()
        print(i)


def main():
    book_reader('book/generated_book.txt')


if __name__ == '__main__':
    main()
