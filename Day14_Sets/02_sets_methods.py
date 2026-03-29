
# union -> combine two sets
set1 = {1, 3, 5, 2, 4, 5, 1, 2}
set2 = {2, 4, 5, 7, 9, 55}

print(set1.union(set2))
print("\n")

print(set1, set2) # not changed, untouched
print("\n")

# update -> update set1 with set 2 value
set1.update(set2)
print(set1)
print("\n")



# intersection -> gives the common values from both sets

cities1 = {"tokyo", "seoul", "delhi", "england"}
cities2 = {"Berlin", "Madrid", "tokyo", "delhi", "seoul", "jakarta"}

print(cities1.intersection(cities2))
print("\n")

cities1.intersection_update(cities2)
print(cities1)
print("\n")

# symmetric_difference -> union - intersection, elements in either, but not both
cities3 = cities1.symmetric_difference(cities2)
print(cities3)

# or
print(cities1.union(cities2) - cities1.intersection(cities2))
print("\n")


# Set difference (-) -> elements in a, but not in b
cities = cities2.difference(cities1)
print(cities)
print("\n")

# isdisjoint() -> check if no common elements
s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4, 5, 6}

print(s1.isdisjoint(s2))
print("\n")

# issubset() -> checks if one set is inside another

print(s1.issubset(s2))
print(s2.issubset(s1))
print("\n")

# issuperset() -> opposite of subset
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print("\n")

# add(value) -> adds a single item to the set
s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4, 5, 6}

s1.add(8)
print(s1)

print("\n")

# remove - removes the element, throws error if element not present

s1.remove(8)
print(s1)
print("\n")


# s2.remove(8)
# print(s2)


# discard() -> gives no error even if element is not present

s2.discard(8) # element not present -> no error
print(s2)

s2.discard(1) # element present -> discarded
print(s2)
print("\n")


# pop() -> removes random element
s1 = {88, 2, 3, 4, 8, 9}
s2 = {1, 2, 3, 4, 5, 6}

s1.pop()
print(s1)

s2.pop()
print(s2)
print("\n")

# copy -> creayes a separate copy

a = {44, 66}
b = a.copy()

print(a)
print(b)
print("\n")


# update -> update with multiple element

a.update([88, 99, 77])
print(a)
print("\n")


# clear() -> empty set
a.clear()
print(a)

