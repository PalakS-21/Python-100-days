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
    print(a + b)
result = add(5, 3)    
print(result)


# return stops the function

def test():
    print("before return!")
    return
    print("Byee!")
test()    