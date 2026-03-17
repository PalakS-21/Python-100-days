# return -> sends a value back from a function to the place where the function was called.

# with return, stores result and can be reused.
def add(a, b):
    return a + b # return a+b to result -> step 2
result = add(5, 4) # function is called -> step 1
result1 = add(54, 46)
print(result) # step3
print(result1)
print(result + result1)

# define → call → calculate → return value → print/use result

# with print, result cannot be reused
def add(a, b):
    print(a + b)  # 8
result = add(5, 3)    
print(result)   # None because function did not send back the result.


# return ends the function

def test():
    print("before return!")
    return
    print("Byee!")
test()    

# even - odd checking with return

num = int(input("Enter a number : "))

def check_even(num):

    if num %2 == 0:
        return "Even"
    if num %2 != 0:
        return "Odd"

print(check_even(num))    


# checking eligibity

age = int(input("Enter a number : "))
def check_eligibility(age):
    if age >= 18:
        return True
    if age < 18:
        return False

print("Eligible : ", check_eligibility(age))    