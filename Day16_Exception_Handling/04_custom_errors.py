# custom error -> creating your own error type.
# raise -> throw an error manually.

# creating custom error
age = 15

if age < 18:
    raise Exception("You are not eligible!")

# with built-in error
num = int(input("Enter any number : "))
