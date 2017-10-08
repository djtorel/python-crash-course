# Write a while loop that prompts users for their name. When they enter
# their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry
# appears on a new line in the file.

file = 'guest_book.txt'
with open(file, 'w') as file_object:
    file_object.write('')

while True:
    name = input("Enter your name (or 'q' to quit): ")
    if name == 'q':
        break
    print("Hello, " + name.title() + "!")
    with open(file, 'a') as file_object:
        file_object.write(name.title() + '\n')
