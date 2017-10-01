# You don’t have to limit the number of tests you create to 10. If you
# want to try more comparisons, write more tests and add them to
# conditional_tests.py. Have at least one True and one False result for
# each of the following:

# • Tests for equality and inequality with strings

# • Tests using the lower() function

# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

# • Tests using the and keyword and the or keyword

# • Test whether an item is in a list

# • Test whether an item is not in a list

print("Is 'thing' == 'thing'? I predict True.")
print('thing' == 'thing')

print("Is 'THING'.lower() == 'thing'? I predict True.")
print('THING'.lower() == 'thing')

stuff = ['thing', 'noise', 'rabble']
print("Is 'flower' in stuff? I predict False.")
print('flower' in stuff)

print("Is 'rabble' not in stuff? I predict False")
print('rabble' not in stuff)
