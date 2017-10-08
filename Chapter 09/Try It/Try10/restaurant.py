"""A module that hosts a class that models a restaurant"""

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