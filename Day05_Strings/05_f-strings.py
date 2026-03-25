
# f-strings -> formatted string

# old way 
name = "palak"
print("Hello " +name)

# f -string
name = "Palak"
print(f"Hello {name}")
# {} -> place where value goes

# with multiple variables
name = "John"
age = 23
print(f"Hello, I am {name} and I am {age} years old.")

# expression
a = 5
b = 8

print(f"Sum is {a+b}")

# using functions
name = "python"
print(f"{name.upper()}")

# formatting numbers

# decimal formatting

pi = 3.14159
print(f"{pi :.2f}") # takes only 2 decimal values only

# percentage
score = 389
total = 500

print(f"{(score/total)*100 :.1f} %")

# if value after decimal is .999, python will round it off to zero.

marks  = 45.999
print(f"{marks:.1f}")  # 46.0

# dictionary / list

data = ["apple", "banana"]
print(f"{data[0]}")