# Make a class called Restaurant. The __init__() method for Restaurant
# should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two
# pieces of information, and a method called open_restaurant() that
# prints a message indicating that the restaurant is open.


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


paulys = Restaurant("paulys pizza", "pizza")
paulys.describe_restaurant()
paulys.open_restaurant()
