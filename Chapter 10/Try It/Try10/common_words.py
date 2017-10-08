# Visit Project Gutenberg (http://gutenberg.org/) and find a few texts
# you’d like to analyze. Download the text files for these works, or
# copy the raw text from your browser into a text file on your computer.

# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the
# number of times 'row' appears in a string:

# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3

# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.

# Write a program that reads the files you found at Project Gutenberg
# and determines how many times the word 'the' appears in each text.

filenames = ['dracula.txt', 'pride_and_prejudice.txt',
             'sherlock_holmes.txt']

for file in filenames:
    try:
        with open(file, encoding='utf8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("The file, " + file + " was not found.")
    else:
        word_count = contents.lower().count('the')
        print("\nThe word 'the' appears in " + file + ", " +
              str(word_count) + " times.")
