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