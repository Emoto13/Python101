import random
from alphabet import alphabet


def create_word():
    length = random.randint(1, 10)
    word = []
    for i in range(length):
        word.append(random.choice(alphabet))
    return "".join(word)


def create_chapter(chapter_number, words_per_chapter):
    words = [f'# Chapter {chapter_number}', '\n']
    for i in range(words_per_chapter):
        words.append(create_word())
        if i % 10 == 0:
            words.append('\n')
    words.append('\n')
    return " ".join(words)


def book_generator(chapters, words_per_chapter):
    for i in range(1, chapters + 1):
        with open('book/generated_book.txt', 'a') as f:
            f.write(create_chapter(i, words_per_chapter))


def main():
    book_generator(10000, 500000)


if __name__ == '__main__':
    main()
