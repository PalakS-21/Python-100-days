
# syntax -> value_if_true if condition else value_if_false

age = 18
print("Adult") if age >= 18 else print ("Minor")

# storing values instead of printing

num = int(input("Enter any number to check whwther it is positive or negative :"))

result = "Positive" if num > 0 else "Negative"

print(result)

# greatest number

a = 5
b = 8

greater = a if a > b else b

print(greater)

# multiple short hand if else

num = int(input("Enter a number to check positive, negaative or zero: "))

result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"

print(result)