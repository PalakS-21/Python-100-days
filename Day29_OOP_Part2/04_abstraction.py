# ABSTRACTION -> Abstraction means hiding the implementation details and showing only the essential features to the user.

from abc import ABC, abstractmethod # to use abstraction

# abc -> abstract base class -> module/library
# ABC -> class inside abc module
# abstractmethod -> Decorator inside the abc module -> @abstractmethod

class Animal(ABC):  # Animal inherits from ABC

    def eat(self): # can have normal class
        print("Eating")

    @abstractmethod # every child must write this method
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")
        # pass

d1 = Dog()

d1.sound()

# ABC makes the class abstract.
# @abstractmethod makes the method abstract, and prevents object creation until child classes implement thet method.

# if a class inherits from ABC but has no @abstractmethod , then also it is an abstract class.
from abc import ABC

class Animal(ABC):
    pass

a1 = Animal()   # Allowed


# @abstractmethod prevents object creation until child classes implement thet method.

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
     
#      @abstractmethod
#      def Car(self):    
#         pass

# v1 = Vehicle()

#---------------------------------------------------------------------

from abc import ABC, abstractmethod

class Vehicle(ABC):
     
     @abstractmethod
     def start(self):    
        pass

# implementation
class Toyota(Vehicle): # Toyota is inherited from Vehicle

    def start(self):
        print("start")
    
    def drive(self):
        print("Driving Fortuner")

v1 = Toyota()
v1.start()
v1.drive()

# In an abstract class, the child class must implement all abstract methods with the same name and compatible parameters.

# Payment App Example

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):

    def pay(self):
        print("Payment through UPI")

class CreditCard(Payment):

    def pay(self):
        print("Payment through Credit Card")

p1 = UPI()
# p2 = CreditCard()

p1.pay()
# p2.pay()