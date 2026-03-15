# A program where a student can do these task :
# 1. Check Voting Eligibility
# 2. Simple Calculator
# 3. Grade Checker
# 4. Exit

name = input("Please enter your name : ")

while True:
    print("\n~~~~~~~~~~~STUDENT UTILITY PROGRAM~~~~~~~~~~~~")
    print("\n1. Check Voting Eligibility")
    print("2. Simple Calculator")
    print("3. Grade Checker")
    print("4. Exit \n")

    choice = input(f"Hello {name}, Please enter your Choice :")

    # CHOICE 1
    if choice == "1":
        age = int(input("Enter your age : "))

        if age >= 18:
            print("You are Eligible to Vote.")
        else:
            print("You are not eligible to Vote.")

    # CHOICE 2            
    elif choice == "2":
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

        op = input("Select the Operation you want to perform (+, -, *, /): ")

        match op:
            case '+':
                print("Result : ", num1 + num2)
            case '-':
                print("Result : ", num1 - num2)
            case '*':
                print('Result : ', num1 * num2)
            case '/':
                if num2 == 0:
                    print("Cannot be divided by Zero")
                print("Result : ", num1 / num2)
            case _:
                print("Invalid Operator")
             
    # CHOICE 3
    elif choice == "3":
        marks = int(input("Enter your marks : "))

        if marks >= 90:
            print(f"{marks} -> Grade : A")
        elif marks >= 75:
            print(f"{marks} -> Grade : B")
        elif marks >= 50:
            print(f"{marks} -> Grade : C")
        else:
            print(f"{marks} -> Grade: Fail")    
             
    # CHOICE 4
    elif choice == "4":
        print("Have a nice day ", name)
        print("Exiting program...")         
        break
    else:
        print("Invalid choice. Try again.")