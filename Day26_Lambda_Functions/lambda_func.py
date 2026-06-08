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

# even, odd

is_even = lambda x: x % 2 == 0

print(is_even(8))

# student percentage

percentage = lambda marks: marks / 500 * 100

print(percentage(430))

# Electricity bill

bill = lambda units: units * 8

print(bill(100))

# shopping discount

discount = lambda price: price - (price * 0.1)

print(discount(3000))

# lambda with map() function

numbers = [1, 2, 3, 4, 5]

# if u wanna double the numbers

result = map(lambda x: x * 2, numbers)

print(list(result))