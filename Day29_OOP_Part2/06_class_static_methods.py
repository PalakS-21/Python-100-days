# @classmethod -> works with the class itself, rather than a particular object.
# it uses cls instead of self.

class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_school): # cls refers to class.
        cls.school = new_school

print(Student.school)

Student.change_school("XYZ School")

print(Student.school)

# @staticmethod -> a normal function kept inside a class because it is related to that class.
# @staticmethod doesn't need self ans cls.

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(Calculator.add(x, y))

# example

class Student:

    school = "ABC School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # normal method
    def show_student(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    # class method
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # static method
    @staticmethod
    def is_pass(marks):
        return marks >= 40

name = input("Enter Student name: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)

s1.show_student()

print("School:", Student.school)

new_school = input("Enter new school: ")
Student.change_school(new_school)

print("New school: ", Student.school)

print("Passed: ", Student.is_pass(marks))