# opening a file -> open()

file = open('mynotes.txt', 'r')

# reading a file -> read()

text = file.read()

print(text)

# closing a file -> close()

file.close()


# writing to file -> write()
# Mode "w" erases old content.

file = open('mynotes.txt', 'w')

file.write("Hello World")

file.close()

# append mode -> 'a' -> keeps old data

file = open('mynotes.txt', 'a')

file.write("\nAppend Mode")

file.close()