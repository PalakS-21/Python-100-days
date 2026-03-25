# docstring -> documentation string
# it explains what function does, what input it takes and what it returns

# it is written just after function def using """ """ or ''' ''', it is not comment.

# creating docstring 

def intro():
    """ heyy!!, this is Docstring."""
    print("Hello Docstring !!")

# accessing docstring with (func.__doc__)
print(intro.__doc__) 
print(type(intro.__doc__)) # str

intro() # calling function
print("\n")


# below is not a docstring
def greet():
    print("Hello Docstring!")
    """ this is docstring """ # ignored, because its not first statement inside function.

print(greet.__doc__) # None
greet()
print("\n")

# ---programs---

# program to add 2 numbers

def add(a, b):
    '''returns the sum of two numbers'''
    return a + b

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

print(f"Result : {add(a, b)}")
print(add.__doc__)
print("\n")

# List Sum

def list_sum(nums):
    """returns the sum of all elements  in the list"""
    return sum(nums)

nums = [1, 4, 66, 7, 20, 100, 322]

print(f"Sum : {list_sum(nums)}")
print(list_sum.__doc__)
print("\n")
