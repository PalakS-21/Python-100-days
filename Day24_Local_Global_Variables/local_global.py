
# global variable -> a variable declared outside all functions.

name = "Pyhton"  # global variable

def greet():
    print(name)

greet()

#--------------------------------------------------------------

# local variable -> variable declared inside the function 


def greet():
    name = "pyhton"   # local variable
    print(name)

greet()

#---------------------------------------------------------------

#NameError -> because variable exists only inside the function.

# def flower_name():
#     flower = "Sunflower"

# flower_name()

# print(flower)


# pyhton checks first -> Inside function -> Outside function.
# local variable gets priority.

#-------------------------------------------------------

# variables with same name

name = "Global"

def check():
    name = "Local" # local variable
    print(name)

check()

print(name) # global variable -> mango


#---------------------------------------------------

# it gives UnboundLocalError.
# python thinks it is creating a local variable x = x + 5

# x = 10

# def demo():
#     x = x + 5 # using before creating -> illegal
#     print(x)

# demo()

#----------------------------------------------------

# global keyword -> allows modifying global variable inside a function.

x = 10

def demo():
    global x    # use global x, don't create local x

    x = x + 5
    print(x)

demo()

#---------------------------------------------------------

count = 0

def increase():
    global count
    count +=1

increase()
increase()
increase()

print(count)