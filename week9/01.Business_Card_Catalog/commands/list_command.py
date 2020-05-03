import sqlite3


def list_users():
    users = get_users_from_the_data_base()
    print_output(users)


def get_users_from_the_data_base():
    connection = sqlite3.connect('business_catalog.db')
    cursor = connection.cursor()
    query = '''SELECT * 
                   FROM users'''
    cursor.execute(query)
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    return users


def format_output(users):
    return "\n\n".join(list(map(mapping_function, users)))


def mapping_function(user):
    return f'{user[0]}. ID {user[0]}, Email: {user[2]}, Full name: {user[1]}'


def print_output(users):
    contacts_message = """
      ############
      ##Contacts##
      ############
      """
    output = format_output(users)

    print(contacts_message)
    print(output)
