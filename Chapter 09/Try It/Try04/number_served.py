# Start with your program from Exercise 9-1 (page 166). Add an attribute
# called number_served with a default value of 0. Create an instance
# called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.

# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number
# and print the value again.

# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any
# number you like that could represent how many customers were served
# in, say, a day of business.


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


restaurant = Restaurant("paulys pizza", "pizza")
print(restaurant.name)
print(restaurant.type)
print("Number served: " + str(restaurant.number_served))
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 2
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(4)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(30)
print("Number served: " + str(restaurant.number_served))
