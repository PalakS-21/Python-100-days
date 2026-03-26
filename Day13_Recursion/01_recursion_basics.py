
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

print(fibbonacci.__doc__)  # docstring
print(fibbonacci(8))
print("\n")