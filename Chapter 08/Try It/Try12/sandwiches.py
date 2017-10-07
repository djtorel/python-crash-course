# Write a function that accepts a list of items a person wants on a
# sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of
# the sandwich that is being ordered. Call the function three times,
# using a different number of arguments each time.


def make_sandwich(*items):
    print("\nThe sandwich ordered has the following items:")
    for item in items:
        print("- " + item.title())


make_sandwich('bacon', 'lettuce', 'tomatoes')
make_sandwich('roast beef', 'cheese')
make_sandwich('meat balls', 'provolone', 'sauce', 'onion')
