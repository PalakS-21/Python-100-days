# methods - built-in functions that help us manipulate the string easily.

#upper() - converts the string to uppercase.
name = "palak"
print(name.upper()) #PALAK

#lower() - converts to lowercase.
surname = "SONI"
print(surname.lower())

#islower() - returns true if string is in lower case, else returns false.
print(name.islower())
print(surname.islower())\

#isupper() - returns true if string is in upper case, else returns false.
print(name.isupper())
print(surname.isupper())

#strip() - removes extra spaces from start and end.
text = "   hey, palak   "
print(text)
print(text.strip())
#lstrip() - removes left spaces
print(text.lstrip())
#rstrip() - removes right spaces
print(text.rstrip())

#find() - returns the index of first occurence.
hello = "Python is fun."
print(hello.find("P")) #0
print(hello.find("fun"))  #10 - starting index of fun
print(hello.find("not")) # returns -1 if not found.

#index() - similar to find(), but it gives ERROR if not found.
hello = "python is fun"
print(hello.index("is"))
# print(hello.index("x")) #error - substring not found.

#replace() - rerplaces part of the string.
str = " I love ice-cream."
print(str.replace("I","We")) # replaces I from We.

#count() - count occurence of a character or word in a word/sentence.
str1 = "banana banana"
print(str1.count("a"))
print(str1.count("b"))
print(str1.count("n"))

#split() - converts string into list [a, b, c, d,...]
fruits = "apple orange mango watermelon grapes banana"
print(fruits.split())

#capitalize() - converts the first letter to uppercase.
blogHeading = "introDUCtion to python."
print(blogHeading.capitalize()) #Introduction to python.

#center() - Centers the string inside given width.
str2 = "Welcome"
print(str2.center(50))

#endswith() - checks if the string ends with the given letter/word.
str3 = "Sky is pink today."
print(str3.endswith(".")) #true
print(str3.endswith("y")) #false

#startswith() - checks if the string starts with given letter/word.
str3 = "It's a beautiful day!"
print(str3.startswith("i")) #false, case-sensitive
print(str3.startswith("I")) #True

#isalnum() - checks if string is alpha-numeric or not.
str3 = "let's learn python."
print(str3.isalnum())
str3 = "palak123456"
print(str3.isalnum())

#isalpha() - checks if the string contain only alphabet from A-Z.
str3 = "alphabet"
print(str3.isalpha())
str3 = "palak986"
print(str3.isalpha())

#isprintable() - returns true if all values in the string are printable, if not, then false.
str = "Happy Birthday!"
print(str.isprintable())
str = "\n" #not printable
print(str.isprintable()) #false

#isspace() - returns true onl;y and only if the dtring contains white spaces, else returns false.
str = "    "
print(str.isspace())
str = "    3  "       #false
print(str.isspace())

#istitle() - returns true only if the first letter of each word of the string is capitalized, else false.
str = "I am learning Python."
#title() - converts the first letter of each word to uppercase.
print(str.title())
print(str.istitle()) #false
str = "I Am Learning Python."
print(str.istitle()) #true

#swapcase() - reverse case of the string.
color = "Magenta"
print(color.swapcase())

print("palak".upper().title())
