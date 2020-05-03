import sqlite3


def get_single_user_from_the_database(entered_id):
    connection = sqlite3.connect('/home/emoto13/Desktop/databases/business_catalog.db')
    query = '''SELECT *  
                  FROM users
                  WHERE id=?'''
    cursor = connection.execute(query, entered_id)
    user = cursor.fetchall()
    connection.commit()
    connection.close()
    if not user:
        raise ValueError("No such user exists")
    return user


def format_output(user, action):
    return create_template_output_for_single_user(user, action)


def create_template_output_for_single_user(user, action):
    options = {
        'get': 'Contact info: ',
        'delete': 'Following contact is deleted successfully: '
    }

    output = f'''
    {options[action]}

    ###############
    Id: {user[0]},
    Full name: {user[1]}
    Email: {user[2]}
    Age: {user[3]}
    Phone: {user[4]}
    Additional info: {user[4] if user[4] else 'Missing'}
    ##############
    '''
    return output
