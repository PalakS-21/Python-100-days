# Numeric Data Types: int, float, complex(a, b)

x = 21
y = -10
print("x : " +str(x))
print("y is negative : "+str(y))

z = 45.99
print("z is float data type : "+str(z))

k = 3 + 4j 
q = complex(3, 4) # alternate way
print(k)
print(q)

# String data type : "text" enclosed in ""

name = "Harry Potter"
house = "Gryffindor" #string
p = "10" #string, not number
print(f"{name} is in {house}")

# Boolean data type - True/False, must start from capital T and F.
is_potterhead = True
print(is_potterhead)

# Sequence data types : list, tuple, dict(dictionary), set

#list - ordered, mutable(changeable), allows duplicate, uses [] brackets
list = ["apple", "banana", "orange", "mango", "'apple",[1, 2, 3]]
print(list)

#tuple - ordered, NOT changeable(immutable), uses () parenthesis
tuple = ("palak", 20, "jabalpur", "pyhton",)
print(tuple)

#dict - dictionary, stores data in key-value pairs, uses {}
dict = {
    "name" : "Hermoine", "age" : 15, "canVote" : True
    }
print(dict)

#set - unordered collection, no duplicates, unique values
set = {1, 2, 3, 3, 4, 2, 5} #duplicates(2, 3) will be removed automatically
print(set)
