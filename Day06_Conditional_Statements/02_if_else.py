#if-else
#else executes when if statement is false.

age = int(input("enter your age : "))
if age >= 18:
    print("You can Vote.")
else:
    print("Underage. You cannot Vote.")
# print("this is out of if-else block")#out of indentation - out of if-else block.

has_id = True
if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry not allowed.")

num = int(input("Enter a number : "))
if (num < 50):
    print(num, " is less than 50.")
else:
    print(num, " is greater than 50.")

#greatest of two number.
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if(num1 > num2):
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num2} is greater than {num1}.")
print("Done.")

#even-odd 
if (num1 %2 == 0) :
    print(num1, " : even")
else:
    print(num1, " : Odd")

#ATM Withdrawal check
balance = 50000
withdraw = int(input("Enter Withdrawal Amount : "))
if withdraw <= balance:
    print("Withdrawal Successful.")
else:
    print("Insufficient Balance.")

#Simple Login System
correct_password = "python143"
entered_password = input("Enter the password : ")
if correct_password == entered_password:
    print("Verified. Login Successful!")
else:
    print("Incorrect password")

# also important
x = 0 # 0 = false
if x:  #if bool(x)
    ## if x executes when bool(x) is True, otherwise else executes
    print("True")    
else:
    print("False")

x = 1 #1=true
if x:
    print("yess")
else:
    print("noo")    

print("BYEEEE!!!!")