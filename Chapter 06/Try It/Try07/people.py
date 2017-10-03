# Start with the program you wrote for Exercise 6-1 (page 102). Make two
# new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of
# people. As you loop through the list, print everything you know about
# each person.


people = [
    {
        'first_name': 'john',
        'last_name': 'doe',
        'age': 38,
        'city': 'scottsdale',
    }, {
        'first_name': 'jane',
        'last_name': 'smith',
        'age': 23,
        'city': 'phoenix',
    }, {
        'first_name': 'jill',
        'last_name': 'parsons',
        'age': 42,
        'city': 'flagstaff'
    }
]

for person in people:
    print("\nName: " + person['first_name'].title() + " " +
          person['last_name'].title())
    print("Age: " + str(person['age']))
    print("City: " + person['city'].title())
