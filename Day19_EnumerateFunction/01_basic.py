# enumerate gives -> (index, value) for every item

fruits = ["Apple", "Mango", "Orange"]

for fruit in enumerate(fruits):
    print(fruit) # (0, 'Apple') -> packed

# unpacking the tuple
for index, fruit in enumerate(fruits):
    print(index, fruit)  # 0 Apple -> unpacked


# if we don't want to start indexing from zero..
for index, fruit in enumerate(fruits, start = 1):
    print(index, fruit)


# strings with enumerate
name = "Palak"

for index, char in enumerate(name):
    print(index, char)

# founding position
name = "python"

for index, char in enumerate(name):
    if char == 'h':
        print("Found at:", index)

# student list
students = ["Harry", "John", "Steve"]

for roll, student in enumerate(students, start=1):
    print(f"Roll No {roll}: {student}")