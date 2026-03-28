
# recursion -> when a function calls itself.

# factorial(5) - 5*4*3*2*1
# factorial(4) - 4*3*2*1
# factorial(3) - 3*2*1
# factorial(2) - 2*1
# factorial(1) - 1

# factorial(n) = n * factorial(n - 1)

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1) # function calling itself
    
print(factorial(5)) 
print(factorial(4))  
print(factorial(1)) 
print("\n")

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 1  -> returns back


# --------------------------------------

# finnonacci series
# 0, 1, 1, 2, 3, 5, 8, 13, 21......

# sum of two previous number = next number
# 1st num = 0, 2nd num = 1

def fibbonacci(n):
    """Returns nth fibbonacci series"""
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibbonacci(n-1) + fibbonacci(n - 2) # recursion

print(fibbonacci(8))
print(fibbonacci.__doc__)  # docstring
print("\n")

#-----------------------------------------------------

# sum of digits

num = int(input("Enter any digit  : "))

def sum_digits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digits(num//10)

print(f"Sum of digits in {num} = {sum_digits(num)}")    
print("\n")

#-------------------------------------------------------

# reverse a string

string = input("Enter a string to reverse : ")

def reverse_string(string):
    if string == "":
        return ""
    
    return reverse_string(string[1 : ]) + string[0]

print(reverse_string(string))
print("\n")

#-----------------------------

# sum of numbers 1 to n
# 1 + 2 + 3 + 4 + 5 +.........+ n

# ex : sum of 4 = 4 + 3 + 2 + 1
# 4 + 3 + sum(2)
# 4 + 3 + 2 + sum(1)
# 4 + 3 + 2 + 1

num = int(input("Enter any number : "))

def sum_num(num):
    if num == 0:
        return 0
    return num + sum_num(num - 1)

print(sum_num(num))
print("\n")

#-------------------------------------------

# count number of digits in a number

num = int(input("Enter a number : "))

def count_digit(num):
    if num == 0:
        return 0
    return 1 + count_digit(num // 10)

print(f"No. of digits in {num} = {count_digit(num)}")
