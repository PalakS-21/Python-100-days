
# input() always returns string, we need to typecast if we want numbers.
 
age = int(input("Enter your age : "))
print("Your age is : ",age)
print(type(age))  #int

rollNum = input("Enter your roll number : ")
print("Roll Number : ",rollNum)
print(type(rollNum)) #str

x = input("Enter first number : ")
y = input("Enter second number : ")
# x, y = input("Enter 2 numbers : ") #taking multiple inputs in a single line
print(x + y) # it will give string, ex-if x=2 & y=3, result will be 23, because input always returns a string.
print(int(x) + int(y)) # here it will give the sum of two numbers.

height = float(input("Enter height in meters : "))
print("Your height is : ", height)
print(type(height))  #float