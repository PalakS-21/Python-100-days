# POLYMORPHISM -> Polymorphism allows the same method or function name to perform different tasks depending on the object.

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