# Write a while loop that asks people why they like programming. Each
# time someone enters a reason, add their reason to a file that stores
# all the responses.

file = 'programming_poll.txt'
with open(file, 'w') as file_object:
    file_object.write('')

while True:
    answer = input("Enter a reason you like programming " +
                   "(or 'q' to quit): ")
    if answer == 'q':
        break
    with open(file, 'a') as file_object:
        file_object.write(answer + '\n')
