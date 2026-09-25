# set comprehension
# syntax -> {expression for item in iterable}

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 3, 2}

squares = {x * x for x in numbers}

print(squares)

even = { x for x in numbers if x % 2 == 0}

print(even)

n = int(input("Enter a number: "))

squares = {x * x for x in range(1, n + 1)}

print(squares)