"""A module that stores information about Admin and privileges"""

from user import User


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
