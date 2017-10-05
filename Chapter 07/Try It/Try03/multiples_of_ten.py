# Ask the user for a number, and then report whether the number is a
# multiple of 10 or not.

number = input("Input a number: ")
number = int(number)
if number % 10 == 0:
    print("The number " + str(number) + " is divisible by 10.")
else:
    print("The number " + str(number) + " is not divisible by 10.")
