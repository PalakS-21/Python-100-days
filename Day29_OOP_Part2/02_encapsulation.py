
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


# 2. PROTECTED -> protected member is intended to be used inside the class and by its child classes, still accessible from outside.
# it is created using one underscore(_), example : self._name
# Protected is NOT enforced i n python. Protected = Convention.

class Student:

    def __init__(self):
        self._name = "Protected Member"

s1 = Student()

print(s1._name)


# 3. PRIVATE -> private member is intended to be accessed only its own class.
# it is created using double underscore(__)

class Student:

    def __init__(self):
        self.__name = "Private Member"

s1 = Student()

# print(s1.__name) # gives AttributeError

# accessed using Name Mangling
# Python changes the name to discourage direct access and prevent accidental conflicts.

print(s1._Student__name)

# getter -> a method used to read or get the value of a private variable.

class Student:

    def __init__(self):
        self.__age = 20

    def get_age(self):
       return self.__age 
    
s1 = Student()

print(s1.get_age())

# setter -> used to change or set the value of a private variable.

class Student:

    def __init__(self):
        self.__age = 21

    def set_age(self, age):

        if age >= 0:
            self.__age = age
        else:
            print("Invalid Age")

    def get_age(self):
        return self.__age

s1 = Student()

s1.set_age(25)

print(s1.get_age())