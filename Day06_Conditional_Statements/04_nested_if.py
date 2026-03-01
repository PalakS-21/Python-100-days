
#nested if - an if statement inside another if statement.
num = int(input("Enter a number : "))
if(num < 0):
    print("Number is negative.")
elif (num > 0):
    if(num <= 10):
        print("Number is between 1-10.")
    elif (num <= 20):
        print("Number is between 11-20.")
    else:
        print("Number is greater than 20.")
else:
    ("Number is Zero.")        


marks = int(input("Enter your marks : "))
passed_exam = True
if passed_exam:
    print("Eligiblr for Admission.")
    if marks >= 80:
        print("Eligible for Scholarship.")
else:
    print("Not Eligible")        

# Check 1
#    ↓
# If True → Check 2
#    ↓
# If True → Action
