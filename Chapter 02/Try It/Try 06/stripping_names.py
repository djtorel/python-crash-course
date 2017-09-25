# Store a person's name, and include some whitespace characters at the
# beginning end of the name. Make sure to use \n and \t at least once.

name = "\t \n\nDominic\n \t\t"

print(name, name, name)

print(name.lstrip(), name.lstrip(), name.lstrip())
print(name.rstrip(), name.rstrip(), name.rstrip())
print(name.strip(), name.strip(), name.strip())
