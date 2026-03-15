
#strings are indexed - position based.

lang = "Python"
#accessing the characters by index.
print(lang[0]) #P, indexing starts from zero - access the first character.
print(lang[1]) #y
print(lang[2]) #t
print(lang[3]) #h
print(lang[4]) #o
print(lang[5]) #n
print("\n")
# print(lang[6]) #throws an error, since index five does not exist.

#negative indexing- accessing the characters from last.
#does not include 0 index.

print(lang[-6]) #P
print(lang[-5]) #y
print(lang[-4]) #t
print(lang[-3]) #h
print(lang[-2]) #o
print(lang[-1]) #n
print("\n")


intro = """Hello!, this is Palak.
I'm learning python,
and it is so interesting."""
#accessing character in multi-line string with the help of loop.
for character in intro:
    print(character)
