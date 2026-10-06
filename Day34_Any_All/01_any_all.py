# any() checks a group of values/conditions and asks if one of them is true.

numbers = [1, 3, 5, 8, 9]

print(any(n > 5 for n in numbers))

# returns true if only one value is true.

values = (False, False, True, False, False)

print(any(values))


print("\n")


# all() asks if all the values are true.

numbers = [2, 4, 6, 8, 22, 44, 66, 42]

print(all(n % 2 == 0 for n in numbers)) # true bcaz all values are even.

numbers = (2, 4, 6, 7, 8, 12)

print(all(n % 2 == 0 for n in numbers)) # false bcz 7 is not even.

# all() returns true only if all values are true

val = [False, False, False]
print(all(val))

val = [True, False, False]
print(all(val))

val = [True, True, True]
print(all(val))
