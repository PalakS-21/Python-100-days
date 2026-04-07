#  exception  -> a error that occurs when your program is runnning. 

# a = input("Enter the number :")
# print(f"Multiplication table of {a} is :")

# for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# # if input is wrong(ex : ps -> input), program will halt here

# print("Some imp line of code")
# print("Byee!!!")


# with exception handling

a = input("Enter the number :")
print(f"Multiplication table of {a} is :")

try:  # code thaat may cause error
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except Exception as e:  # what to do if error occurs
#  print(e) # error print
   print("Sorry, some error occured!!")       


print("Some imp line of code")
print("Byee!!!")
print("\n")

#---------------------------------------------------

try:
    num = int(input("Enteer a number :"))
    print(10/num)
# if num = 0,     
except:  
    print("Error occurerd!")

#----------------------------------------------------

# specific error

try:
    num = int(input("Enter a number : "))
    print(10/num)
except ZeroDivisionError:
    print("Cannot be divided by zero!")
except ValueError:
    print("Invalid Input!")    