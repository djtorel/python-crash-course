# You can use the replace() method to replace any word in a string with
# a different word. Here’s a quick example showing how to replace 'dog'
# with 'cat' in a sentence:

# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'

# Read in each line from the file you just created, learning_python.txt,
# and replace the word Python with the name of another language, such as
# C. Print each modified line to the screen.


filename = 'learning_python.txt'

# lines = []
# with open(filename) as file_object:
#     for line in file_object:
#         lines.append(line.replace('Python', 'C'))

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace('Python', 'C'))