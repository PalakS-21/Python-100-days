# lambda function is a small anonymous function.

# normal function

# def square(x):
#     return x * x

# print(square(5))

# with lambda function
# syntax -> lambda arguments : expression

# square of a number
square = lambda x: x * x

print(square(5))

# add 2 numbers

add = lambda a, b: a + b

print(add(5, 4))

# find maximum of 2 nums

max = lambda a, b: a if a > b else b

print(max(55, 8))