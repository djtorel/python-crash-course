# One common problem when prompting for numerical input occurs when
# people provide text instead of numbers. When you try to convert the
# input to an int, you’ll get a ValueError. Write a program that prompts
# for two numbers. Add them together and print the result. Catch the
# ValueError if either input value is not a number, and print a friendly
# error message. Test your program by entering two numbers and then by
# entering some text instead of a number.

print("Enter two numbers and I will add them for you.")
num1 = input("\nFirst number: ")
num2 = input("Second number: ")

try:
    sum = int(num1) + int(num2)
except ValueError:
    print("One of these is an invalid value.")
else:
    print("The sum of " + num1 + " and " + num2 + " is: " + str(sum))
