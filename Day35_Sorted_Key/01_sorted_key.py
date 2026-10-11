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