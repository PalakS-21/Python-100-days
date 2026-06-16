# class -> Blueprint / template for creating an object.

class Student:
    pass # nothing for bnow

# creating an object 
s1 = Student() # s1 -> object, student -> creating object
print(s1)

# adding attributes
s1.name = "Steve"
s1.age = 20

 # accessing the attributes
print(s1.name)
print(s1.age)

# multiple objects
s2 = Student()
s3 = Student()


# with self
class Person:
    name = "Palak"
    occupation = "Software Engineer"

    def info(self):
        print(f"{self.name} is a {self.occupation}.")
        # self -> current object being createed

a = Person() # object
b = Person()

# a.name = "Ron"
# a.occupation = "HR"
print(a.name, a.occupation)

a.info()

a.name = "harry"
a.occupation = "Accountant"

b.name = "Ritika"
b.occupation = "Dancer"

a.info()
b.info()
