import sqlite3
from queries_constants_create_table import queries
from database_path import database_path


def create_database_and_tables():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    for query in queries:
        cursor.execute(query)

    connection.commit()
    connection.close()
