# Using one of the programs you wrote in this chapter, add several lines to
# the end of the program that do the following:

# • Print the message, The first three items in the list are:. Then use a slice
# to print the first three items from that program’s list.

# • Print the message, Three items from the middle of the list are:. Use a
# slice to print three items from the middle of the list.

# • Print the message, The last three items in the list are:. Use a slice to
# print the last three items in the list.

cubes = [number**3 for number in range(1, 11)]

print("The first three items in the list are:")
for cube in cubes[:3]:
    print(cube)

print("Three items in the middle of the list are:")
for cube in cubes[4:7]:
    print(cube)

print("The last three items in the list are:")
for cube in cubes[-3:]:
    print(cube)
