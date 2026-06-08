# lambda with map() function.
# map() -> applies a function to every element of an iterable.

numbers = [1, 2, 3, 4, 5]

# if u wanna double the numbers

result = map(lambda x: x * 2, numbers)
print(list(result))

result = map(lambda x: x * x, numbers)
print(list(result))

result = map(lambda x: x - 5, numbers)
print(list(result))