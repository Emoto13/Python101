from list_all_free_hours_command import list_all_free_hours


def client_factory(command):
    commands = {
        'list_all_free_hours': list_all_free_hours,
        'list_free_hours': '',
        'save_repair_hour': '',
        'update_repair_hour': '',
        'delete_repair_hour': '',
        'add_vehicle': '',
        'update_vehicle': '',
        'delete_vehicle': '',
        'exit': ''
    }

    return handle_command(command, commands)


def handle_command(command, commands):
    if command not in commands.keys():
        raise ValueError("No such command")
    execute_command = commands[command]
    return execute_command()
