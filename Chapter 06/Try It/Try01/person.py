# Use a dictionary to store information about a person you know. Store
# their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 38,
    'city': 'Scottsdale'
}

print("Name: " + person['first_name'].title() + " " +
      person['last_name'].title())
print("Age: " + str(person['age']))
print("City: " + person['city'])
