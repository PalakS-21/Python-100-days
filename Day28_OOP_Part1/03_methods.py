# method -> a function defined inside a class.

class Student:

    def greet(self):
        print("Hello!")

s1 = Student()

s1.greet()

# with constructor

class Student:

    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hello,", self.name)

s1 = Student("Harry Potter")
s2 = Student("Hermoine")
s3 = Student("Ron")

s1.greet()
s2.greet() # multiple objects
s3.greet()

# bankAccount

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Balance =", self.balance)

account = BankAccount(100000)

account.show_balance()

# calculator

class Calculator:

    def add(self, a, b):
        print(a + b)

c1 = Calculator()

c1.add(30, 80)
