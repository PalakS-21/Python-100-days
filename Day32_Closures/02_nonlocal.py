# nonlocal: Used inside a nested function to modify a variable from the outer function.

def counter():
    count = 0

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
