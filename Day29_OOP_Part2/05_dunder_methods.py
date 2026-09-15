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

# print(s1)
print(repr(s1))

# __len__()
# len(object) is returned.

class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)

t1 = Team(["A", "B", "C", "D"])

print(len(t1))


# __add__()
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

m1 = Money(300)
m2 = Money(600)

print(m1 + m2)

# __eq__()
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age =age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

e1 = Employee("Harry Potter", 18)
e2 = Employee("Harry Potter", 18)

print(e1==e2)
