# Start with your class from Exercise 9-1. Create three different
# instances from the class, and call describe_restaurant() for each
# instance.


class Restaurant():
    """A simple way to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and type attributes"""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Print the name and type of restaurant"""
        print("The restaurant " + self.name.title() +
              " serves " + self.type.title() + " style cuisine.")

    def open_restaurant(self):
        """Print that the restaurant is now open"""
        print(self.name.title() + " is now open!")


restaurant_01 = Restaurant('foo', 'bar')
restaurant_01.describe_restaurant()

restaurant_02 = Restaurant('lees', 'chinese')
restaurant_02.describe_restaurant()

restaurant_03 = Restaurant('tonys', 'italian')
restaurant_03.describe_restaurant()
