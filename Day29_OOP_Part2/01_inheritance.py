# one class can acquire the properties and methods of another class.

class Animal:

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class Dog(Animal):            # inheritance
    def bark(self):
        print("Barking")

d1 = Dog()
d1.eat()
d1.sleep()
d1.bark()

#-----------------------------------------------------------

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(Self):
        print("The default language is Python.")

e1 = Employee("Rosh", 432)
e1.showDetails()

e2 = Programmer("Steve", 864)
e2.showDetails()

e2.showLanguage()

#--------------------------------------------------

class Person:

    def __init__(self):
        print("Person")

class Student(Person):
    
    def __init__(self):
        print("Student")

s1 = Student()

# If Child has constructor -> Only Child constructor runs

# If Child has NO constructor -> Parent constructor runs

# we use super().__init__ -> to work both constructor

class Person:

    def __init__(self):
        print("Person Constructor")

class Student(Person):
    
    def __init__(self):
        super().__init__()
        print("Student Constructor")

s1 = Student()

#-----------------------------------------------------------------

# METHOD OVERRIDING

# Parent and Child have methods with the same name.
# Child's method replaces (overrides) the Parent's method.

class Animal:

    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):

    def sound(self):    # method name is same -> overriding
        super().sound() # super() is used to call the parent's method.
        print("Dog barks!!")

d1 = Dog()
d1.sound()

# a1 = Animal()
# a1.sound()

# if child doesn't override, then python uses parent's method

class Animal:

    def sound(self):
        print("Animal makes a sound 2")
    
class Cat(Animal):
    pass

c1 = Cat()
c1.sound()