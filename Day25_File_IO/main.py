# opening a file -> open()

file = open('mynotes.txt', 'r')

# reading a file -> read(), mode -> 'r'

text = file.read()

print(text)

# closing a file -> close()

file.close()


# writing to file -> write()
# Mode "w" erases old content.

# file = open('mynotes.txt', 'w')

# file.write("Hello World")

# file.close()

# append mode -> 'a' -> keeps old data

file = open('mynotes.txt', 'a')

file.write("\nAppend Mode")

file.close()

# read line by line

file  = open('mynotes.txt')

for line in file:
    print(line)

file.close()

# readline() -> only first line is read.

file = open("mynotes.txt")

print(file.readline())

file.close()

# readlines() -> returns a list.

file = open("mynotes.txt")

print(file.readlines())

# better code

file.close()

with open('mynotes.txt') as file:
    content = file.read()

print(content)

# notes app example

# note = input("Enter note:")

# with open('mynotes.txt', 'a') as file:
#     file.write(note + "\n")


# tell() -> tells us where is the cursor right now in the file.

file = open('mynotes.txt', 'r')

print(file.tell()) #0 -> beacuse the cursor starts at the beginning.

file.close()

# after reading -> 

file = open('mynotes.txt', 'r')

print(file.read(25)) # reads 5 character

print(file.tell())

file.close()

# seek() -> moves the cursor to a specific position.

file = open('mynotes.txt', 'r')

file.seek(6)

print(file.read())

file.close()

# example

file = open('mynotes.txt', 'r')

print("cursor posiiton initially:", file.tell())

print(file.read(5)) # only reads 5 character.

print("Cursor postion after read(5) :", file.tell())

print(file.seek(0))

file.seek(0) # moves cursor back to position 0.

print("Cursor position after seek(0) :",file.tell())

file.close()