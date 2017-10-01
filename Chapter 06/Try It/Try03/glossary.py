# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.

# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store
# their meanings as values.

# • Print each word and its meaning as neatly formatted output. You
# might print the word followed by a colon and then its meaning, or
# print the word on one line and then print its meaning indented on a
# second line. Use the newline character (\n) to insert a blank line
# between each word-meaning pair in your output.

glossary = {
    'variable': 'Used to store some sort of data or information.',
    'list': 'A collection of data or information that can be iterated.',
    'struct': 'An immutable collection of data that can be iterated.',
    'dictionary': 'A collection of data stored as key value pairs.',
    'string': 'A series of text characters.'
}

print("Variable:\n\t" + glossary['variable'])
print("\nList:\n\t" + glossary['list'])
print("\nStruct:\n\t" + glossary['struct'])
print("\nDictionary:\n\t" + glossary['dictionary'])
print("\nString:\n\t" + glossary['string'])
