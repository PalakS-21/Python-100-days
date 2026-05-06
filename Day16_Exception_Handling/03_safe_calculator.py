
def calculator():
        try:
            print("Welcome to safe calculator")

            num1 = int(input("Enter first number :"))
            num2 = int(input("Enter second number :"))

            op = input("Enter operation (+, -, *, /): ")

            if op == '+':
                print("Result :", num1 + num2)
            
            elif op == '-':
                print("Subtraction Result : ", num1 - num2)

            elif op == "*":
                print("Multiplication Result :", num1 * num2)
            
            elif op == '/':
                print("Division Result : ", num1 / num2)
            
            else:
                print("Invalid operator!")

        except ZeroDivisionError:
            print("Cannot be divided by zero!")  

        except ValueError:
            print("Invalid input! Please enter numbers only.")


        finally:
            print("Program ended")

while True:
    calculator()

    choice = input("Do you want to continue? (yes/no): ").lower()

    if choice == "no":
        print("Exiting program...")
        break

