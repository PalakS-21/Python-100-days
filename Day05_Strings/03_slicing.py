#string slicing - slicing a part of string.
# string[start:end] - start = 0, & end is excluded.

fruit = "Watermelon"
print("length : ",len(fruit))
print(fruit[0:5]) #Water, includes 0 but not 5.
print(fruit[5:10]) #melon
print(fruit[2:7]) #terme
print(fruit[5:7]) #me

print(fruit[0:-2])
print(fruit[0:len(fruit)-2]) #same as above
print(fruit[:-2]) #also same

print(fruit[-8:-4])
print(fruit[-10:-5])

print(fruit[::-1]) # reverse the string
print(fruit[::2]) # [start:end:step]
print(fruit[1:9:3])