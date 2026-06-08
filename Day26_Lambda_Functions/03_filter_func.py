#FILTER -> filter()
# filter() -> select only the elements which satisfy a condition.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# select only even numbers

even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))

# select students who got marks >= 40.

marks = [30, 45, 22, 78, 65, 99, 35]

students = filter(lambda x: x >= 40, marks)
print(list(students))

# filter() returns original elements, not the values produced by lambda.

numbers = [1, 2, 3, 4, 5]

result = filter(lambda x: x * 2, numbers)
print(list(result)) # [1, 2, 3, 4, 5] bcoz filter() expects boolean answer