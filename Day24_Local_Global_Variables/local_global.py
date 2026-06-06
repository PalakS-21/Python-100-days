
# global variable -> a variable declared outside all functions.

name = "Pyhton"  # global variable

def greet():
    print(name)

greet()

def greet():
    name = "pyhton"   # local variable
    print(name)

greet()

#NameError -> because variable exists only inside the function.

# def flower_name():
#     flower = "Sunflower"

# flower_name()

# print(flower)


# pyhton checks first -> Inside function -> Outside function.
# local variable gets priority.

name = "Global"

def check():
    name = "Local" # local variable
    print(name)

check()

print(name) # global variable -> mango