#  exception handling -> 

a = input("Enter the number :")
print(f"Multiplication table of {a} is :")

for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
# if input is wrong(ex : ps -> input), program will halt here

print("Some imp line of code")
print("Byee!!!")
