
# List is used to store multiple values in a single variable

list1 = [1, 2, 3, 4, 5]
print(list1)

data = ["palak", 20, True, "python", "jabalpur", 8.2]
print(data)

fruits = ["apple", "banana", "mango", "litchi"]
print(fruits)

# indexing -> accessing elements from list
# index starts from 0 (zero)
print(fruits[0]) #appple
print(fruits[1]) #banana
print(fruits[2]) #mango
print(fruits[3]) #litchi

# len -> length of list
print(len(fruits))

# changing values in list
fruits[1] = "orange"
print(fruits)

# negative indexing
print(fruits[-2]) 
print(fruits[len(fruits) - 2]) # positive index
print(fruits[4-2]) # positive index
print(fruits[2])  # positive index

# loop in list
for fruit in fruits:
    print(fruit)

# if - else in list
if "apple" in fruits:
    print("Yes")
else:
    print("No") 

if "ppl" in "apple":
    print("True")
else:
    print("False")    

# slicing 
nums = [90, 75, 93,23, 13, 75, 32, 44]
print(nums[:])
print(nums[1:])
print(nums[:4])
print(nums[0:5])
print(nums[1:4])    

# step slicing 
print(nums[0:6:3])
# [starting index : last index : step index]  
print(nums[1:7:2])

# list comprehension

lst = [i for i in range(11)]
print(lst)

lst = [i*i for i in range(11)]
print(lst)

lst = [i for i in range(11) if i %2==0]
print(lst)