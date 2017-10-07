# Start with your program from Exercise 9-1 (page 166). Add an attribute
# called number_served with a default value of 0. Create an instance
# called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.


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


restaurant = Restaurant("paulys pizza", "pizza")
print(restaurant.name)
print(restaurant.type)
print("Number served: " + str(restaurant.number_served))
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 2
print("Number served: " + str(restaurant.number_served))
