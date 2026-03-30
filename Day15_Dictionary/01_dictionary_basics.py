
# dictionary -> ordered collection of data items
# dictinary items are key-value pairs.
# dictionary is mainly used to do mapping.

# creating a dictionary

fruit ={
    "fruit_name" :"Mango",
    "fruit_colour" : "Yellow",
    "fruit_price" : 60 ,
}
print(fruit)
print("\n")

# accessing values - > using keys
print(fruit["fruit_name"]) # single
print(fruit["fruit_colour"], fruit["fruit_price"]) # multiple

print(fruit.get("fruit_name"))

# if accessing a key using [] that is not present, it throws error
# example
# print(fruit["taste"]) # -> error

print("\n")

# to remove error, we use get() -> error free
print(fruit.get("taste")) # None

# to get all the keys - dict.keys()
print(fruit.keys())
print("\n")

# to get all values -> dict.values()
print(fruit.values())
print("\n")


# looping in dictionary

# loop keys
for key in fruit :
    print(key) # prints only keys

print("\n")

# loop in keys()
for key in fruit.keys():
    print(f"The {key} is {fruit[key]}.")    

print("\n")

# loop values
for value in fruit.values(): 
    print(value) # prints only values

print("\n")

# loop both keys, values
for key, value in fruit.items():
    print(key,":", value)    # iterates and give 

print("\n")
print(fruit.items()) # gives (key, value) pairs

print("\n")

for key, value in fruit.items():
    print(key + str(value))

