# Modify your except block in Exercise 10-8 to fail silently if either
# file is missing.

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(filename + ' has these contents:')
        print(contents.rstrip() + '\n')
