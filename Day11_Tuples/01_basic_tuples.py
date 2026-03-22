
# creating tuples

tup = (1, 2, 3)
print(tup)

# creating a tuple with single element

tup = (1,) # comma(,) after one element is mandatory
print(tup)
print(type(tup))  # tuple

# without comma(,) the type changes to int
# example

tup = (5)
print(type(tup))  # int
print(tup)

# accessing elements 

tup = (1, 3, 4, 6, 78, 8, 31)
print(tup[0]) # 0 index
print(tup[1])
print(tup[2])
print(tup[6])

# negative index
print(tup[-1])
print(tup[-6])          # 3
print(tup[len(tup) - 6])  # 3

# tuple is immmutable

t = (1, 2, 3, 4)
t[0] = 0 # error
