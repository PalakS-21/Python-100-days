
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
# t[0] = 0 # error

# check for item in tuple

if 10 in t:
    print("Yess, 10 is present in tuple.")
else:
    print("Not present!!!")


# loop in tuple

tup1 = (3, 6, 9, 12, 15)
for t in tup1:
    print(t)    


# slicing - creates a new tuple

tup = (1, 2, 45, 3, 4, 22)
print(tup[0:5]) # from index 0 to index 4, last index is not included.
print(tup[:4]) # blank index = 0, from starting
print(tup[1:]) # till last index

# negative slicing
print(tup[-3:])

print(tup[: : -1]) # reverse tuple

print(tup[1: : 2]) # start idx : last idx : jump step
print(tup[: : 3])

# loop + slicing

for t in tup[0:4]:
    print(t)

# we use buit-in functions instead of methods with tuples, bcoz tuples are immutable.
# we must first convert a tuple to a list to use methods.

t = (1, 2, 3, 4)

# len() function -> length of tuple
print(len(t))

# max() & min() 
print(max(t)) # 4
print(min(t)) # 1

# sum() -> sum of all tuple elements
print(sum(t))

# sorted() -> sorts the tuple
t = (3, 6, 1, 5, 2, 4)
print(type(t), sorted(t)) # returns list

# list to tuple conversion
l = [1, 2, 3]
t = tuple(l)

print(t)

# tuple methods - mainly 2

# 1. count() -> counts how many timems a value appears
t = (1, 2, 5, 44, 2, 3, 2, 1)
print(t.count(2))
print(t.count(3))

# 2. index() -> finds position of element
print(t.index(3)) # index of first occurence
print(t.index(44))
print(t.index(2, 3, 8))

# t.append(55) # error, bcoz tuples are immutable