# ABSTRACTION -> Abstraction means hiding the implementation details and showing only the essential features to the user.

from abc import ABC, abstractmethod # to use abstraction

# abc -> abstract base class

class Animal(ABC):

    @abstractmethod # every child must write this method
    def sound(self):
        pass

class Dog(Animal):

    # def sound(self):
        # print("Bark")
        pass

d1 = Dog()

# d1.sound()
