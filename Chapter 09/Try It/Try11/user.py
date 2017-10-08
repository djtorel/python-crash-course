"""A module that stores classes that represents users"""

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


class Privileges():
    """Store and show information about privileges"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user',
                           'can modify post', 'can see deleted posts']

    def show_privileges(self):
        """Show privileges set for user"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)


class Admin(User):
    """Stores and presents admin information"""

    def __init__(self, first_name, last_name, user_name, email):
        """
        Initialize from parent class
        Set privileges for admin
        """
        super().__init__(first_name, last_name, user_name, email)
        self.privileges = Privileges()