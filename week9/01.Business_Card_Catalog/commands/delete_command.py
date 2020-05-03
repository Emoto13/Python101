import sqlite3
from commands.templates_for_single_user import create_template_output_for_single_user, get_single_user_from_the_database, format_output


def delete_user_by_id():
    entered_id = input('Enter id: ')
    user = get_single_user_from_the_database(entered_id)[0]
    delete_user_from_the_database(entered_id)
    print(format_output(user, 'delete'))


def delete_user_from_the_database(entered_id):
    connection = sqlite3.connect('business_catalog.db')
    cursor = connection.cursor()
    query = '''DELETE FROM users
                WHERE id=?'''
    cursor.execute(query, entered_id)
    connection.commit()
    connection.close()
