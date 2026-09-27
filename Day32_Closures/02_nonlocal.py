# nonlocal: Used inside a nested function to modify a variable from the outer function.

# Outer Function
def counter():
    # count = 0
    count = int(input("Enter starting count: "))

    # Inner Function
    def increase():
        nonlocal count
        count += 1
        print(count)

    return increase

my_counter = counter()

my_counter() # 1
my_counter() # 2
my_counter() # 3
my_counter()

# closure   → remember
# nonlocal  → modify that remembered variable