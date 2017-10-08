# An ice cream stand is a specific kind of restaurant. Write a class
# called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version
# of the class will work; just pick the one you like better. Add an
# attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors. Create an instance of
# IceCreamStand, and call this method.


class Restaurant():
    """A simple way to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and type attributes"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the name and type of restaurant"""
        print("The restaurant " + self.name.title() +
              " serves " + self.type.title() + " style cuisine.")

    def open_restaurant(self):
        """Print that the restaurant is now open"""
        print(self.name.title() + " is now open!")

    def set_number_served(self, num_customers):
        """Set the number of customers served"""
        self.number_served = num_customers

    def increment_number_served(self, num_served):
        """Increment self.number_served by num_served amount"""
        self.number_served += num_served


class IceCreamStand(Restaurant):
    """A simple representation of an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize from parent class
        Set flavors attribute
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Chocolate', 'Vanilla Bean', 'Cookies \'n Cream']

    def describe_flavors(self):
        """Prints the flavors available at the ice cream stand"""
        print("\nFlavors of ice cream: ")
        for flavor in self.flavors:
            print("- " + flavor.title())


ice_cream_stand = IceCreamStand('Stone Cold', 'ice cream')
ice_cream_stand.describe_flavors()
