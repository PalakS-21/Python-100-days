 # break means immediately stop the loop and exit it.

for i in range(1,7) : #1 2 3 4 5 6 
    if i == 5:
        break
    print(i) # 1 2 3 4 

numbers = [10, 20, 30, 40, 50, 60]
for n in numbers :
    if n == 30:
        print(n, "Number Found!")
        break

x = 1
while x <= 10:
    if x == 6:
        break
    print(x)
    x += 1 #it stops when x = 6.

# break only stops the nearest loop.
for i in range(5):
    for j in range(5):
        if j == 1:
            break
        print(i, j)
print("Out of Loop")

for i in range(5):
    if i == 3:
        break
    print(i)
    print("Loop running...")
print("\n")

#find first even number in the list
numbers = [3, 5, 7, 65, 20, 56, 100]
for i in numbers :
    if i % 2 == 0:
        print("First even Number :", i)
        break

# while True:
#     password = input('Enter password : ' )
#     if password == 'python123':
#         print("Verified")
#         break

# guess the number game
num = 7
while True:
    guess = int(input("Guess the number : "))
    if guess == num:
        print("Woww!! You Guessed it correct.")
        break
    else:
        print("Wrong Guess!! Try again.")    

#______________________________________________________________________________________

# continue statement
#continue means : skip the current iteration and move to next one.

for i in range(5):  # 1 2 3 4
    if i == 3:
            continue
    print(i) # 1 2 4 

# skip negative numbers
numbers = [3, 5, -2, 55, -4, -44, -12, 50, 98]
for number in numbers:
    if number < 0:
        continue
    print(number)

for i in range(1, 10):
    if i == 5:
        continue
    print(i)
    print('Running..')


x =0 
while x < 6:
    x += 1
    if x == 3:
        continue
    print(x)


# skip empty input
for i in range(2):  #number of attempts
    name = input("Enter your name : ")

    if name == "": # empty
        continue

    print("Hello, ",name)


for i in range(1, 12):
    if i == 3:
        continue
    if i == 11:
        break

    print(i)