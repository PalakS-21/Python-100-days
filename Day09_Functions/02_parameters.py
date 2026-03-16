
# parameters allow functions to accept values and work with different inputs.
# a aparameter is a variable inside the function that receives a value.

def greet(name):
    # here name is parameter
    print("Hello", name)

# calling the function with argument
greet('Palak') 
# calling the function multiple times  
greet("Harry Potter") 
greet('Alexa')
greet("Steve")

# function with two parameters

# function to add two numbers.
def add(a, b):
    print("sum : ", a+b)
add(10, 55)    # a = 10, b = 55
add(5, 5)      # a = 5, b = 5

# function to calculate average to 2 numbers
def average(x, y):
    print("Average : ", (x + y)/2)
average(34, 67)
average(20, 30)    
average(y = 30, x = 50) 

# string as parameter
def introduce(name, city):
    print("My name is ", name)
    print("I live in ", city)

introduce("Palak", "Jabalpur")

# function to calculate square of a number
def square(num):
    print("Square of",num, "=", num*num)
square(5)    
square(75)

# function with user input
def fruit(name):
    print("Fruit :", name)

user = input("Your fruit : ")
fruit(user)

# *parameter or *args (tuple)
# (*parameter) allows a function to accept multiple arguments and stores them as a tuple.

def ex(*numbers):
    print(numbers)
    print(type(numbers))
ex(2, 3, 6, 2)

def sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(total)    
sum(10, 40, 50, 30, 20) 

def example(*args):
    print(args)
example(1,2,3)  

# **parameter or **kwargs (dictionary)
# allows a function to store many key value pairs in dictionary form.

def demo(**data):
    print(data)
demo(name="Steve", age=20, city = "Delhi")

# accessing the data
def show(**data):
    print("Name :", data["name"])
    print("Age :", data["age"])
show(name = "john", age = 23)    

# **kwargs -> professional way -> many key-value pairs -> dictionary
def account(**kwargs):
    print("Username :", kwargs['username'])
    print("Password :", kwargs['password'])
account(username = "palak", password = 123456)


