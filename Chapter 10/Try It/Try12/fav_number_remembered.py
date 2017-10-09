# Combine the two programs from Exercise 10-11 into one file. If the
# number is already stored, report the favorite number to the user. If
# not, prompt for the user’s favorite number and store it in a file.
# Run the program twice to see that it works.

import json


def get_favorite_number():
    """Get stored favorite number if it exists."""

    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_number():
    """Get a new favorite number and store it"""

    filename = 'favorite_number.json'
    number = input("What's your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)

    print("\nI will remember that " + number + " is your favorite number.")


def favorite_number():
    """
    Print out favorite number if it exists,
    if not call get_new_number()
    """
    number = get_favorite_number()

    if number:
        print("Your favorite number is " + number + "!")
    else:
        get_new_number()


favorite_number()
