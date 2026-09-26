# Closure: An inner function that remembers variables from its outer function.

def outer():
    message = "Hellooo!!!"

    # Inner func uses the variable from outer()
    def inner():
        print(message)

    # Return the inner function
    return inner

# outer() runs and returns inner
my_function = outer()

# my_function now refers to inner()
my_function()