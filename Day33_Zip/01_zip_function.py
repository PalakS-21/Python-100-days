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