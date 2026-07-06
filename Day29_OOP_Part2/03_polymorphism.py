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

    def add(self, a, b, c):
        print(a + b + c)
 
c1 = Calculator()

c1.add(10, 20, 30)
# c1.add(10, 2) # TypeError : missing 'c

