# You just heard that one of your guests can't make the dinner, so you need
# to send out a new set of invitations. You'll have to think of someone else to
# invite.

# Start with your program from exercise 3-4. Add a print statement at the end
# of your program stating the name of the guest who can't make it.

# Modify your list, replacing the name of the guest who can't make it with the
# name of the new person you are inviting.

# Print a second set of invitation messages, one for each person who is still
# in your list.

guests = ['Albert Einstein', 'Isaac Newton', 'Alan Turing']

print("Dear " + guests[0] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[1] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[2] + ",\n\tI humbly request you to join me for dinner.")

print(guests[1] + " says they cannot make it.")

del guests[1]
guests.append('Isaac Asimov')

print("Dear " + guests[0] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[1] + ",\n\tI humbly request you to join me for dinner.")
print("Dear " + guests[2] + ",\n\tI humbly request you to join me for dinner.")
