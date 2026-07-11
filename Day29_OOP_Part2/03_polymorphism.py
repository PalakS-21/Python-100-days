# POLYMORPHISM -> Polymorphism allows the same method or function name to perform different tasks depending on the object.
# method overriding -> same name, different objects
class Person:

    def introduce(Self):
        print("I am a Person.")

class Student(Person):

    def introduce(Self):
        print("I am a Student.")

p1 = Person()
s1 = Student()

p1.introduce()
s1.introduce()


# Method Overloading -> multiple methods with same name but with different parameters in the same class.

class Calculator:

    def add(Self, a, b):
        print(a + b)

    def add(self, a, b, c):  # if method name is same, replace the old one and keep the new one
        print(a + b + c)
 
c1 = Calculator()

c1.add(10, 20, 30)
# c1.add(10, 2) # TypeError : missing 'c

# methods to achieve method overloading in python using c = 0 or *args
class Calculator:

    def add(self, a, b, c = 0): 
        print(a + b + c)

c2 = Calculator()

c2.add(44, 66)
c2.add(22, 22, 33)

# using *args

class Calculator:

    def add(self, *numbers):  # *numbers accepts any  number of arguments.
        print(sum(numbers))

c3 = Calculator()

c3.add(11, 11)

c3.add(5, 5, 5)

c3.add(60, 40, 100, 55)