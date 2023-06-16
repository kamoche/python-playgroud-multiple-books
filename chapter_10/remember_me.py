import json


def get_stored_username(file_name):
    """Get username if available"""
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def create_new_user(file_name):
    username = input("What's your name:")
    with open(file_name, 'w') as f_obj:
        json.dump(username.title(), f_obj)
    return username


def greet_user():
    """Greet the user name"""
    file_name = "username.json"

    username = get_stored_username(file_name)
    if username:
        print("Welcome back," + username + "!")
    else:
        username = create_new_user(username)
        print("I will remember you next time you come back " + username.title())



greet_user()
