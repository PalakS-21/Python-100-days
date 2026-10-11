# sorted() arranges items in order and returns a new list.

numbers = (2, 14, 6, 7, 25, 5, 9, 1, 44, 32, 11)

result = sorted(numbers)

print(result)
print(numbers) # original remains unchanged

letters = "gfhidcabe"
print(sorted(letters))

# sorts words alphabetically
names = ["Harry", "Steve", "Jane", "Aerbie"]
print(sorted(names))



# key= tells python which value to use for sorting.

names = ["Harry", "Steve", "Jane", "Aerbie", "Bella"]
# key= len tells python to sort words by their length.
print(sorted(names, key=len))

# A custom function or lambda can be used as key

def last_digit(n):
    return n % 10

numbers = [22, 11, 35, 43, 16]
# 22 % 10 = 2
# 11 % 10 = 1
# 35 % 10 = 5
# 43 % 10 = 3
# 16 % 10 = 6
print(sorted(numbers, key=last_digit))

# output contains the original items, not the key values.

# key with lambda
numbers = [22, 11, 35, 43, 16, 24]

print(sorted(numbers, key=lambda n: n % 10))
