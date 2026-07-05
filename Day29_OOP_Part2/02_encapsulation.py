
# ENCAPSULATION -> Data + Methods + Data Protection

# 1. Bundle data and methods together.
# 2. Restrict direct access to data.

# Access Specifiers -> 1. Public
#                      2. Protected
#                      3. Private

# 1. PUBLIC -> public member can be accessd from anywhere.

class Student:
    def __init__(self):
        self.name = "Public Member"

s1 = Student()

print(s1.name)


