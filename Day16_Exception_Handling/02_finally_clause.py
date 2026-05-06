
# finally clause -> always runs, no matter what.

try:
    print("hello")
finally:
    print("This always runs.")

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
    print("Program finished.")