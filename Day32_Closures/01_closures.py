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

# example -> creating customized function
def discount(discount_percent):

    def calculate(price):
        return price - (price * discount_percent / 100)

    return calculate

student_discount = discount(10)
festive_discount = discount(20)

print(student_discount(1000))
print(festive_discount(1000))