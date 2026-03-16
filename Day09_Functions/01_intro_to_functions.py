
#def -> keyword to define a function
def greet():   # greet -> function name
    print("Hello World!")

greet()  # calling the function

def introduction():
    print("Hello, this is Palak")
    print("I am learning Python")
    print("This is Day 9.")

greet()
greet()
introduction()

def make_line():
    print("------------------------")
    print("Loading")
    print("------------------------")

make_line()
greet()
make_line()
introduction()
make_line()

# function with loop
for i in range(3):
    greet()

def sum():
    print(5+4)

sum()
# A function executes its code every time it is called