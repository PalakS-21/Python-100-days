
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

def add(a, b):
    print("sum : ", a+b)
add(10, 55)    
add(5, 5)