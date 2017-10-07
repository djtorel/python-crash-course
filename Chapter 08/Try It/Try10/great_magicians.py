# Start with a copy of your program from Exercise 8-9. Write a function
# called make_great() that modifies the list of magicians by adding the
# phrase the Great to each magician’s name. Call show_magicians() to see
# that the list has actually been modified.


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    i = 0
    for magician in magicians:
        magicians[i] = magician + " The Great"
        i += 1


magicians = ['Houdini', 'Penn', 'Teller']
make_great(magicians)
show_magicians(magicians)
