# Now that you know how to loop through a dictionary, clean up the code
# from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and
# values. When you’re sure that your loop works, add five more Python
# terms to your glossary. When you run your program again, these new
# words and meanings should automatically be included in the output.

glossary = {
    'variable': 'Used to store some sort of data or information.',
    'list': 'A collection of data or information that can be iterated.',
    'struct': 'An immutable collection of data that can be iterated.',
    'dictionary': 'A collection of data stored as key value pairs.',
    'string': 'A series of text characters.'
}

for term, definition in glossary.items():
    print(term + ":\n\t" + definition)
