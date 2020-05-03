from commands.templates_for_single_user import create_template_output_for_single_user, \
    get_single_user_from_the_database, format_output


def get_user_by_id():
    entered_id = input('Enter id: ')
    user = get_single_user_from_the_database(entered_id)[0]
    print(format_output(user, 'get'))
