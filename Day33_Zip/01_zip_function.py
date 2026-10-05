# zip() -> used to combine elements from two or more iterables position-wise.

names = ["Palak","Rhea", "Jane", "Ariana" ]
marks = [88, 79, 80]

result = zip(names, marks)

print(list(result))
# Ariana has no corresponding mark, so its excluded.

names = input("Enter names separated by space: ").split()
marks = list(map(int, input("Enter marks separated by space: ").split()))

result = zip(names, marks)

print(list(result))

# zip() with a for loop

names = ["Palak","Rhea", "Jane", "Ariana" ]
marks = [88, 79, 80]

for name, mark in zip(names, marks):
    print(name, mark)
    print(f"{name} scored {mark} marks.")

# zip() with list, tuple
names = ["Patrick", "Lisbon", "Steve"]
marks = (100, 95, 90)
grades = ["A+", "A", "B"]

for name, marks, grade in zip(names, marks,grades):
    print(name, marks, grade)


# with string
letters = "ABCD"
numbers = (1, 2, 3, 4, 5)

for letter, number in zip(letters, numbers):
    print(letter, number)