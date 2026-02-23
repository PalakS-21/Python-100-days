# Typecasting : conversion of one data type to another

# 1.Implicit typecasting : python automatically converts one data type to another without any command.
# lower-order data type converted to higher level data type.
a = 5 # a converted to int
print(a)
print(type(a))
b = 4.2 # b converted to float
print(b)
print(type(b))
c =  a + b
print(c) # c converted to float autoatically, as it is float addition
print(type(c))

# 2.Explicit typecasting : conversion of one data type into another data type, done via developer or programmer
# uses built-in conversion funtions - int(), float(), hex(), oct(), str(), etc.
string = "12"
num = 5
string_num = int(string) #string to int
sum = num + string_num
print("sum : ", sum)
print(type(sum))

#int to string
num = 50
num_str = str(num)
print(num_str) # "50"
print(type(num_str))\

#float to int
float1 = 5.0
num_int = int(float1)
print(num_int)
print(type(num_int))