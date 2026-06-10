# is (identity operator) vs == (equality operator)

a = 10
b = 10

# == -> checks whether values are equal.
print(a==b) 

# is -> checks whether both variables refer to same object in memory.
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # True -> same values
print(a is b) # False -> different memory

# same object

a = [1, 2, 3, 4]
b = a

print(a == b)
print(a is b)


a = None
b = None

print(a == b)
print(a is b)


# using id() to know memory of the objects

a = [2, 4, 6]
b = [2, 4, 6]

print(id(a))
print(id(b))

x = "John"
y = "John"

print(x == y)
print(x is y)