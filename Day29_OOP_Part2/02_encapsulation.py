
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


# 2. PROTECTED -> protected member is intended to be used inside the class and by its child classes.
# it is created using one underscore(_), example : self._name
# Protected is NOT enforced.

class Student:

    def __init__(self):
        self._name = "Protected Member"

s1 = Student()

print(s1._name)
