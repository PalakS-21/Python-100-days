                                       
# normal way to create list using loop 

nums = [1, 2, 3, 4, 5]

square = []

for n in nums:
    square.append(n * n)

print(square)    

# with list comprehension
# list ccomprehension -> short and clean way to create lists using a loop.

nums = [1, 2, 3, 4, 5]

squares = [n * n for n in nums]

print(squares)

# with condition

nums = [1, 2, 3, 4, 5, 6, 7, 8]

even = []

for n in nums:
    if n % 2 == 0:
        even.append(n)

print(even)        