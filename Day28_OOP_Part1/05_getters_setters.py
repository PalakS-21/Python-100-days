# getter -> access data

class Student:

    def __init__(self, age):
        self._age = age

    @property   # @property -> creates getter
    def age(self):
        return self._age
    
s1 = Student(20)

print(s1.age)

# setter -> used to modify data with validation

class Student:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):

        if value > 0:
            self._age = value

        else:
            print("Invalid Age")

s1 = Student(25)

s1. age = 30

print(s1.age)

# @property creates an attribute called age.
# Therefore the actual data is usually stored in _age.