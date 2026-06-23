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

