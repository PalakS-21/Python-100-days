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

# DUCK TYPING -> Python cares about what an object can DO, not what type it IS.
# Python checks Behavior, not Type.

class Dog:

    def speak(self):
        print("Bark!")

class Cat:

    def speak(self):
        print("Meoww!")

def make_sound(animal):
    animal.speak()

d1 = Dog()

c1 = Cat()

make_sound(d1)

make_sound(c1)

# if method doesn't exist then,..

class Car:

    def drive(self):
        print("Driving")

c1 = Car()

# make_sound(c1) # 'Car' object has no attribute 'speak'