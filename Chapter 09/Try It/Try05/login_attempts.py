# Add an attribute called login_attempts to your User class from
# Exercise 9-3 (page 166). Write a method called
# increment_login_attempts() that increments the value of login_attempts
# by 1. Write another method called reset_login_attempts() that resets
# the value of login_attempts to 0.

# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was
# incremented properly, and then call reset_login_attempts(). Print
# login_attempts again to make sure it was reset to 0.


class User():
    """Stores and presents user information"""

    def __init__(self, first_name, last_name, user_name, email):
        self.f_name = first_name
        self.l_name = last_name
        self.u_name = user_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Print out information about the user"""
        print("\nName: " + self.f_name.title() + " " + self.l_name.title())
        print("Username: " + self.u_name)
        print("Email: " + self.email)

    def greet_user(self):
        """Print a greeting for the user"""
        print("\nHello " + self.f_name.title() + "!")

    def increment_login_attempts(self):
        """Increments login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0"""
        self.login_attempts = 0


user_01 = User('bob', 'smith', 'bsmith', 'bsmith@gmail.com')

user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
print("Login attempts: " + str(user_01.login_attempts))

user_01.reset_login_attempts()
print("Login attempts: " + str(user_01.login_attempts))
