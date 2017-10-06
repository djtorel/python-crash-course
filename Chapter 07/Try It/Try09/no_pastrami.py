# Using the list sandwich_orders from Exercise 7-8, make sure the
# sandwich 'pastrami' appears in the list at least three times. Add
# code near the beginning of your program to print a message saying the
# deli has run out of pastrami, and then use a while loop to remove all
# occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami
# sandwiches end up in finished_sandwiches.

sandwich_orders = ['tuna', 'pastrami', 'club', 'blt', 'pastrami',
                   'hamburger', 'roast beef', 'pastrami', ]
finished_sandwiches = []

print("The deli has run out of pastrami!")

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    if sandwich == 'pastrami':
        print("Sorry, we are out of pastrami, and cannot make your sandwich.")
    else:
        print("Now making your " + sandwich + " sandwich.")
        finished_sandwiches.append(sandwich)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
