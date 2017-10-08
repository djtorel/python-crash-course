# Store the User class in one module, and store the Privileges and Admin
# classes in a separate module. In a separatefile, create an Admin
# instance and call show_privileges() to show that everything is still
# working correctly.

from admin import Admin

admin = Admin('dom', 'torr', 'dtorr', 'dtorr@gmail.com')
admin.privileges.show_privileges()
