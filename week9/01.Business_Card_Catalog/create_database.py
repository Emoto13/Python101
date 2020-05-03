import sqlite3


def create_database():
    connection = sqlite3.connect('/home/emoto13/Desktop/databases/business_catalog.db')
    cursor = connection.cursor()
    query = '''CREATE TABLE IF NOT EXISTS users
    (id INTEGER primary key AUTOINCREMENT unique not NULL,
    full_name varchar(50) unique not NULL,
    email varchar(50) unique not NULL,
    age integer Not NULL, 
    phone varchar(50) not NULL,
    additional_info TEXT)'''
    cursor.execute(query)
    connection.commit()
    connection.close()
