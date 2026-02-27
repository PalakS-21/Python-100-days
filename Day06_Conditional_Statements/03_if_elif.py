
#elif - else if
# In if-elif chain, only the first True condition executes.

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#important rule - order matters
#wrong order
marks = 82
if marks >= 55:
    print("Pass")
elif marks >= 75:
    print("Distinction")
#correct order - high to low
if marks >= 75:
    print("Distinction")
elif marks >= 55:
    print("Pass")
#always check bigger condition first

#checking the type of number
num = int(input("Enter the number : "))
if num < 0:
    print("Number is Negative.")
elif num == 0:
    print("Number is Zero.")
else:
    print("Number is Positive.")

#movie ticket
age = int(input("Enter your age : "))
if age < 12:
    print("Ticket Price : 100")
elif age < 60:
    print("Ticket price : 200")
else:
    print("Ticket price : 150")