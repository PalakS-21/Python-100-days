
#taking operator and numbers as input from user.

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
op = input("Enter the operation to be performed (+, -, *, /) : ")

if op == '+':
    print("Addition : ", num1+num2)
elif op == '-' :
    print("Subtraction : ", num1-num2)
elif op == '*':
    print("Multiplication : ",num1*num2)
elif op == '/':
    print("Division : ", num1/num2)
else:
    print("Invalid Operator.")


