import hashlib
import sqlite3
from constants import SYMBOLS, INSERT_QUERY, GET_MESSAGE_QUERY, SECRET_MESSAGE


def make_it_secret(message):
    return hashlib.md5(message.encode()).hexdigest()


def create_database(cursor, connection):
    cursor.execute('''CREATE TABLE IF NOT EXISTS predishnoto_reshenie_vajeshe
                      (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                        message VARCHAR(10) NOT NULL UNIQUE,
                        encrypted_message VARCHAR(50) NOT NULL UNIQUE)
                      ''')
    connection.commit()


def insert_data(cursor, connection):
    for a in SYMBOLS:
        message_one = a
        cursor.execute(INSERT_QUERY, (message_one, make_it_secret(message_one)))
        for b in SYMBOLS:
            message_two = f'{message_one}{b}'
            cursor.execute(INSERT_QUERY, (message_two, make_it_secret(message_two)))

            for c in SYMBOLS:
                message_three = f'{message_two}{c}'
                cursor.execute(INSERT_QUERY, (message_three, make_it_secret(message_three)))

                for d in SYMBOLS:
                    message_four = f'{message_three}{d}'
                    cursor.execute(INSERT_QUERY, (message_four, make_it_secret(message_four)))

                    for e in SYMBOLS:
                        message_five = f'{message_four}{e}'
                        cursor.execute(INSERT_QUERY, (message_five, make_it_secret(message_five)))
    connection.commit()


def decrypt_message(cursor, connection):
    words = SECRET_MESSAGE.split("\n")
    res = []
    for word in words:
        cursor.execute(GET_MESSAGE_QUERY, (word, ))
        decrypted_word = cursor.fetchall()
        res.append("".join(decrypted_word[0]))
        connection.commit()
    return res


def main():
    connection = sqlite3.connect('/home/emoto13/Desktop/databases/iskam_si_birata.db')
    cursor = connection.cursor()

    create_database(cursor, connection)
    insert_data(cursor, connection)
    res = decrypt_message(cursor, connection)
    print(res)
    connection.close()


if __name__ == '__main__':
    main()
