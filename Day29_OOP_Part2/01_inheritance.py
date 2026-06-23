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