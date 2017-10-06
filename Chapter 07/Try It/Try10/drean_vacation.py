# Write a program that polls users about their dream vacation. Write a
# prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the
# poll.

poll_answers = {}
active_poll = True

while active_poll:
    name = input("\nEnter your name: ")
    poll_answers[name] = input("Enter your dream vacation: ")
    to_continue = input("Would you like to make another entry? (yes/no) ")
    if to_continue == 'no':
        active_poll = False

print("\n --- POLL RESULTS ---")
for name, answer in poll_answers.items():
    print("The dream vacation for " + name.title() +
          " would be a trip to " + answer.title() + ".")
