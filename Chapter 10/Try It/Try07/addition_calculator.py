# Wrap your code from Exercise 10-6 in a while loop so the user can
# continue entering numbers even if they make a mistake and enter text
# instead of a number.

while True:
    print("Enter two numbers and I will add them for you.")
    print("Enter 'q' to quit.")
    num1 = input("\nFirst number: ")
    if num1 == 'q':
        break
    num2 = input("Second number: ")
    if num2 == 'q':
        break

    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print("One of these is an invalid value.")
    else:
        print("The sum of " + num1 + " and " + num2 + " is: " +
              str(sum) + "\n")
