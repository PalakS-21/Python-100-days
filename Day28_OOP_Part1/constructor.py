# constructor -> special method that runs automatically when an object is created.

class Student:

    def __init__(self):  # initialization
        print("Student object created")


s1 = Student()

# constructor runs automatically.

# custructor with parameters

class Student:

    def __init__(self, name):
        print(name)

s1 = Student("Riya")

# multiple paramerters

class Student:

    def __init__(self, name, age):
        print(name)
        print(age)

s1 = Student("Harry", 21)

# saving Data in object

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Palak", 20)

print(s1.name)
print(s1.age)