
# union -> combine two sets
set1 = {1, 3, 5, 2, 4, 5, 1, 2}
set2 = {2, 4, 5, 7, 9, 55}

print(set1.union(set2))

print(set1, set2) # not changed, untouched

# update -> update set1 with set 2 value
set1.update(set2)
print(set1)

