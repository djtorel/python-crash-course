# Write a loop that prompts the user to enter a series of pizza toppings
# until they enter a 'quit' value. As they enter each topping, print a
# message saying you’ll add that topping to their pizza.

# I am also choosing to add all the toppings to a list and list all of
# the toppings at the end when user types quit

toppings = []
prompt = "Please enter in a toping you would like, or 'quit' when done: "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("I am adding " + topping + " to your toppings.")
        toppings.append(topping)

message = "Your chosen toppings are: "
for topping in toppings:
    message += topping.title() + ", "
message = message[:-2] + "."
print(message)
