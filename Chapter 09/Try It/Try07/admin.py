# An administrator is a special kind of user. Write a class called Admin
# that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores
# a list of strings like "can add post", "can delete post",
# "can ban user", and so on. Write a method called show_privileges()
# that lists the administrator’s set of privileges. Create an instance
# of Admin, and call your method.


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


class Admin(User):
    """Stores and presents admin information"""

    def __init__(self, first_name, last_name, user_name, email):
        """
        Initialize from parent class
        Set privileges for Admin
        """
        super().__init__(first_name, last_name, user_name, email)
        self.privileges = ['can add post', 'can delete post', 'can ban user',
                           'can modify post', 'can see deleted posts']

    def show_privileges(self):
        """Show privileges set for user"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)


admin = Admin('dom', 'torr', 'dtorr', 'dtorr@gmail.com')
admin.show_privileges()
