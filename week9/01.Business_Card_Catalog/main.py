from event_handler import enter_command
from create_database import create_database


def main():
    create_database()
    try:
        enter_command()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
