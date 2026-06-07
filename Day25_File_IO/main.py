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

note = input("Enter note:")

with open('mynotes.txt', 'a') as file:
    file.write(note + "\n")