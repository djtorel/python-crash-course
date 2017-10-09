# The final listing for remember_me.py assumes either that the user has
# already entered their username or that the program is running for the
# first time. We should modify it in case the current user is not the
# person who last used the program.

# Before printing a welcome back message in greet_user(), ask the user
# if this is the correct username. If it’s not, call get_new_username()
# to get the correct username.

import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.


def get_stored_username():
    """Get stored username if available."""

    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def verify_user(username):
    if username:
        verified = input("Are you " + username + "? (y/n) ")
    else:
        return False

    if verified == 'y':
        return True
    elif verified == 'n':
        return False
    else:
        verify_user(username)


def greet_user():
    """Greet the user by name."""

    username = get_stored_username()
    verified = verify_user(username)
    if verified:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
