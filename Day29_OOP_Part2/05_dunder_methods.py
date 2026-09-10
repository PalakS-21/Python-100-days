# Dunder -> Double Underscore

# python special methods which starts and ends with __ (double underscore).

# 1. __str__()
# __str__() converts/represents object as text.
# user-friendly representation

# without __str__()
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Palak", 20) # output - <__main__.Student object at 0x000002A4752B6A50>
# this means, this is a student object, but we have not told what text it should display for it.

print(s1)

# with __str__()
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age= age

    def __str__(self):
        return f"{self.name}, {self.age}"

s1 = Student("Harry Potter", 14)

print(s1)

# 2. __repr__()
# __repr__() is about representing an object, but its purpose is slightly different

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age= age

    def __str__(self):
        return f"{self.name}, {self.age}"

    # __repr__()
    def __repr__(self):
        return f"Student('{self.name}', {self.age})"

s1 = Student("Harry Potter", 14)

print(s1)
print(repr(s1))