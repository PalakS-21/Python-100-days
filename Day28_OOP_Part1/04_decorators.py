def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

@decorator
def greet():
    print("Hello")

greet()

# 1. decorator() takes a function
# 2. wrapper() adds extra code
# 3. return wrapper
# 4. @decorator applies it

# LOGIN SYSTEM


def login_required(func):

    def wrapper():
        print("Checking Login...")
        func()
    
    return wrapper

@login_required
def view_profile():
    print("Profile Opened")

@login_required
def edit_profile():
    print("Profile Edited")

view_profile()
edit_profile()