# Write a function called city_country() that takes in the name of a
# city and its country. The function should return a string formatted
# like this:

# "Santiago, Chile"

# Call your function with at least three city-country pairs, and print
# the value that’s returned.


def city_country(city, country):
    return city.title() + ', ' + country.title()


print(city_country('phoenix', 'unites states of america'))
print(city_country('hong kong', 'china'))
print(city_country('london', 'england'))
