# dictionary
numbers = {}

for i in range(1, 6):
    numbers[i] = i * i

print(numbers)

# with dictionary comprehension

numbers = { i: i * i for i in range(1, 6)}

print(numbers)

# squares
n = int(input("Enter a number: "))

squares = {x: x * x for x in range(1, n+1)}

print(squares)

# with condition
numbers = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

result = {key: value for key, value in  numbers.items() if value > 20}

print(result)

# key-value pair