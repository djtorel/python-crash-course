# A movie theater charges different ticket prices depending on a
# person’s age. If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10; and if they are over
# age 12, the ticket is $15. Write a loop in which you ask users their
# age, and then tell them the cost of their movie ticket.

prompt = "\nEnter your age, or type 'quit' to exit: "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        elif age > 12:
            price = 15

        print("The cost of admission for age " + str(age) +
              " is $" + str(price) + ".")
