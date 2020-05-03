import sqlite3
from database_path import database_path
from query_constants import query_get_free_hours_by_date


def list_free_hours_by_date(date):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(query_get_free_hours_by_date, (date, ))
    output = cursor.fetchall()
    connection.commit()
    connection.close()
    print(output)
