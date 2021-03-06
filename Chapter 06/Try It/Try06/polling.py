# Use the code in favorite_languages.py (page 104).

# • Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that
# are not.

# • Loop through the list of people who should take the poll. If they
# have already taken the poll, print a message thanking them for
# responding. If they have not yet taken the poll, print a message
# inviting them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

should_poll = [
    'edward',
    'jen',
    'bill',
    'erin',
]

for person in should_poll:
    if person in favorite_languages:
        print("Thank you " + person.title() + ", for taking the poll!")
    else:
        print(person.title() + ", I invite you to take our poll!")
