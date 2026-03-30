
# dictionary -> ordered collection of data items
# dictinary items are key-value pairs.

# creating a dictionary

fruit ={
    "fruit_name" :"Mango",
    "colour" : "Yellow",
    "price" : 60 ,
}
print(fruit)
print("\n")

# accessing values - > using keys
print(fruit["fruit_name"])
print(fruit["colour"])
print(fruit["price"])
print(fruit.get("fruit_name"))

# if accessing a key that is not present, it throws error
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

for key in fruit :
    print(key)