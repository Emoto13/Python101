import sqlite3
from database_path import database_path
from query_constants import query_get_all_free_hours


def list_all_free_hours():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(query_get_all_free_hours)
    output = cursor.fetchall()
    connection.commit()
    connection.close()
    print(output)
