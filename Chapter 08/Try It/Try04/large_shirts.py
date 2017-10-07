# Modify the make_shirt() function so that shirts are large by default
# with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a
# different message.


def make_shirt(size='large', text='I love python'):
    print("\nA " + size + " sized shirt with the message, '" +
          text + "', will be made.")


make_shirt('extra large', 'Hello World!')
make_shirt(text='Foo', size='medium')

make_shirt()
make_shirt('medium')
