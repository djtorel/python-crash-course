# You just found a bigger dinner table, so now more space is available. Think
# of three more guests to invite to dinner. Add a print statement to the end of
# your program informing people that you found a bigger dinner table.

# Use insert() to add one new guest to the beginning of your list.

# use insert() to add one new guest to the middle of your list.

# use append() to add one new guest to the end of your list.

# Print a new set of invitation messages, one for each person in your list.

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
