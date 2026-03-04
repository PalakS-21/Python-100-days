# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

#with for loop
for i in range(1, 5):
    print(i)
    #stops before 11, that is 10.
    #range(start, stop) -> always stops one number before stop.   

for i in range(6):  #starts from zero, stops at 5
    print(i)
print("\n")

for i  in range(1, 10, 4):  #range(start, stop, step)
    print(i)


print("\n")
# for loop -> when you know how many times to repeat.

name = "Palak"
for i in name:
    print(i)

fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)
    for i in fruit:
        print(i)
