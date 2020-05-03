from event_handler import handle_command


def enter_command():
    command = input('Enter command: ').lower()
    return handle_command(command)
