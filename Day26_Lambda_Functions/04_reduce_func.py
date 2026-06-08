# reducee() 
# applies a function repeatedly on the elements of an iterable and reduces them to a single value
# reduce() must be imported.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x,y: x + y, numbers)

print(result)

# result = 10 
# x = 1
# y = 2
# x + y = 3
# x = 3
# y = 3
# 3 + 3 = 6
# x = 6
# y = 4
# 6 + 4 = 10

# syntax -> resuce(function, iterable)

# multiplication

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x * y, numbers)
print(result)

# reduce() : Many -> One