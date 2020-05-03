from create_database_and_tables import create_database_and_tables
from client_factory import client_factory
from list_free_hours_by_date_command import list_free_hours_by_date


def main():
    create_database_and_tables()
    list_free_hours_by_date('03-05-2020')


if __name__ == '__main__':
    main()
