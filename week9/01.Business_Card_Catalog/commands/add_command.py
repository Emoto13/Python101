import sqlite3


def add_business_card():
    values = get_business_card_information()
    add_user_to_database(values)


def get_business_card_information():
    user_name = input('Enter user name: ')
    email = input('Enter email: ')
    age = int(input('Enter age: '))
    phone = input('Enter phone number: ')
    additional_information = input('Enter additional information: ')
    return user_name, email, age, phone, additional_information


def add_user_to_database(values):
    connection = sqlite3.connect('business_catalog.db')
    cursor = connection.cursor()
    query = '''INSERT INTO users (full_name, email, age, phone, additional_info)
                    VALUES (?, ?, ?, ?, ?)
                '''
    cursor.execute(query, values)
    connection.commit()
    connection.close()
