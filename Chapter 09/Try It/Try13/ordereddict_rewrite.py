# Start with Exercise 6-4 (page 108), where you used a standard
# dictionary to represent a glossary. Rewrite the program using the
# OrderedDict class and make sure the order of the output matches the
# order in which key-value pairs were added to the dictionary.

from collections import OrderedDict

glossary = OrderedDict([
    ('variable', 'Used to store some sort of data or information.'),
    ('list', 'A collection of data or information that can be iterated.'),
    ('struct', 'An immutable collection of data that can be iterated.',),
    ('dictionary', 'A collection of data stored as key value pairs.'),
    ('string', 'A series of text characters.'),
])


for term, definition in glossary.items():
    print(term + ":\n- " + definition + "\n")
