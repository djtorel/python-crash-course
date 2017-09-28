# You just found out that your new dinner table won't arrive in time for the
# dinner, and you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner

# Use pop() to remove guests from your list one at a time until only two names
# remain in your list. Each time you pop a name from your list, print a message
# to that person letting them know you're sorry you can't invite them to dinner

# Print a message to each of the two people still on your list, letting them
# know they're still invited.

# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

guests = ['Albert Einstein', 'Isaac Newton', 'Alan Turing']

print("Dear " + guests[0] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[1] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[2] + ",\n\tI humbly request you to join me for dinner.")

print("Oh, wait! It looks like we have room for 3 more guests!")

guests.insert(0, 'Isaac Asimov')
guests.insert(2, 'Richard Feynman')
guests.append('Leonardo DaVinci')

print("Dear " + guests[0] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[1] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[2] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[3] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[4] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[5] + ",\n\tI humbly request you to join me for dinner.")

uninvited = guests.pop()
print("Sorry, " + uninvited + ", I do not have enough room for you now.")
uninvited = guests.pop()
print("Sorry, " + uninvited + ", I do not have enough room for you now.")
uninvited = guests.pop()
print("Sorry, " + uninvited + ", I do not have enough room for you now.")
uninvited = guests.pop()
print("Sorry, " + uninvited + ", I do not have enough room for you now.")

print("Dear " + guests[0] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[1] + ",\n\tI humbly request you to join me for dinner.")

del guests[0]
del guests[0]

print(guests)
