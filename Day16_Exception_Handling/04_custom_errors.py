# custom error -> creating your own error type using raise keyword.
# raise -> throw an error manually.

# creating custom error
# age = 15

# if age < 18:
#     raise Exception("You are not eligible!")

# with built-in error
# num = int(input("Enter any number : "))

# if num < 0:
#     raise ValueError("Negative numbers not allowed!")

# print(num)

a = int(input("Enter any number between 5 and 9: "))


if(a<5 or a>9 ):
    raise ValueError("Value should be between 5 and 9")


# creating custom error
class NegativeNumberError(Exception):
    pass # nothing inside for now

try:
    num = int(input("Enter any non-negative number :"))

    if num < 0:
        raise NegativeNumberError("Negative number entered! Try again.")

    print("Valid number")

except NegativeNumberError as e:
    print("Custom Error: ", e)

# password too short error
class PasswordTooShortError(Exception):
    pass

try:
    password = input("Enter password: ")

    if len(password) < 6:
        raise PasswordTooShortError("Password must be at leat 6 characters! Try again!")
    
    print("Password accepted!")

except PasswordTooShortError as e:
    print(e)    

# InvalidUsernameError
class InvalidUsernameError(Exception):
    pass

try:
    username = input("Enter username: ")

    if not username.isalpha():
        raise InvalidUsernameError("Invalid Username! Username should only contain alphabets.")
    
    print("Username verified.")

except InvalidUsernameError as e:
    print(e)