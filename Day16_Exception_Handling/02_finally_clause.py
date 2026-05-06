
# finally clause -> always runs, no matter what.

try:
    print("hello")
finally:
    print("This always runs.\n")

# if error occurs
# try:
#     print(10 / 0)
# finally:
#     print("This still runs.") 
#     #throws error after this

try:
    num = int(input("Enter a number :"))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot be divided by zero.")

finally:
    print("Program finished.\n")

# finally with return statement

def test():
    try:
        return 1
    finally: 
        print("Inside finally\n")

print(test()) # finally runs before return actually happens


def test():
    try:
        return 1
    finally: # finally overrides previous return 1
        return 2

print("\n",test())

# try + except + finally

def check():
    try:
        print("\nA")
        x = 10 / 0
    except:
        print("C")
        return 30
    finally:
        print("B")

print(check())