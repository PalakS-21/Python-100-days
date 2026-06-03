# import math as m
# import hello
# import random
# import datetime


# print(m.sqrt(9))
# print(m.pi)
# print("\n")


# # print("Main file running")
# hello.greet()

# print(random.randint(1, 100))
# print("\n")

# print(datetime.date.today())

#--------------------------------------------------------------------

# banking app example
import account
from transaction import deposit
from transaction import withdrawl

account.show_balance()

amount = int(input("Enter the amount to Deposit: "))
new_balance = deposit(10000, amount)

print("Available Balance :", new_balance)

with_amount = int(input("Enter amount to withraw:"))
new_balance = withdrawl(new_balance, with_amount)

print("Updated Balance:", new_balance)

#---------------------------------------------------------------------
