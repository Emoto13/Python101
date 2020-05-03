from commands.add_command import add_business_card
from commands.list_command import list_users
from commands.get_command import get_user_by_id
from commands.delete_command import delete_user_by_id
from commands.help_command import execute_help_command


def enter_command():
    command = input('Enter command: ')
    return handle_command(command)


def handle_command(command):
    commands = {'add': add_business_card,
                'list': list_users,
                'get': get_user_by_id,
                'delete': delete_user_by_id,
                'help': execute_help_command}

    return handle_wrapper(command, commands)


def handle_wrapper(command, commands):
    if command not in commands.keys():
        raise ValueError('No such command')

    execute_command = commands[command]
    return execute_command()
