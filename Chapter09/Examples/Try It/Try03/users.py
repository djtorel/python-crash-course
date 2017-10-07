# Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically
# stored in a user profile. Make a method called describe_user() that
# prints a summary of the user’s information. Make another method called
# greet_user() that prints a personalized greeting to the user.

# Create several instances representing different users, and call both
# methods for each user.


class User():
    """Stores and presents user information"""

    def __init__(self, first_name, last_name, user_name, email):
        self.f_name = first_name
        self.l_name = last_name
        self.u_name = user_name
        self.email = email

    def describe_user(self):
        """Print out information about the user"""
        print("\nName: " + self.f_name.title() + " " + self.l_name.title())
        print("Username: " + self.u_name)
        print("Email: " + self.email)

    def greet_user(self):
        """Print a greeting for the user"""
        print("\nHello " + self.f_name.title() + "!")


user_01 = User('bob', 'smith', 'bsmith', 'bsmith@gmail.com')
user_01.describe_user()
user_01.greet_user()

user_02 = User('jane', 'doe', 'jdoe', 'jdoe@gmail.com')
user_02.describe_user()
user_02.greet_user()

user_03 = User('albert', 'einstein', 'aeinstein', 'aeinstein@gmail.com')
user_03.describe_user()
user_03.greet_user()
