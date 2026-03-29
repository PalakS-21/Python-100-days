# Set - collection of unique elements, well defined objects.
# set is unordered
# set - {}

my_set = {1, 2, 3, 4, 2, 1}
print(my_set)  # {1, 2, 3, 4} -> duplicate values get removed.

# set is unordered - no indexing

unorderd_set = {"python", 3.13, True, 21, False, "language", 5.9}
print(unorderd_set) # items of set occur in random order, hence it can't be accessed using index numbers.

# print(unorderd_set[0]) # error


# empty set -> type dictionary
set1 = {}
print(type(set1))  # dict

# creating empty set
set1 = set()
print(type(set1))  # set