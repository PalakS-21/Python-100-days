# Students marks manager

total_marks = 0

def add_marks(marks):
    global total_marks
    total_marks += marks

add_marks(60)
add_marks(88)
add_marks(91)

print("Total Marks:", total_marks)
print("Average:", total_marks / 3)

#------------------------------------------------------------------------

# Bank Account

balance = 100000

amount = int(input("Enter the amount to be withdrawn:"))

def withdraw(amount):
    global balance
    
    if amount <= balance:
        balance -= amount
        print("Withdrawn Amount:", amount)
    else:
        print("Insufficient Balance")

withdraw(amount)

print("Remaining Balance:", balance)


amount = int(input("Enter the amount to Deposit:"))


def deposit(amount):
    global balance

    balance += amount
    print("Deposited Amount: ", amount)

deposit(amount)

print("Remaining Balance:", balance)
print("\n")

#------------------------------------------------------------------

# Shopping Cart

cart = []

item = input("Enter products to add in the Cart: ")

def add_item(item):
    cart.append(item)

add_item(item)

print(cart)