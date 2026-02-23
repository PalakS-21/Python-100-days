
#strings are indexed - position based.

name = "Palak"
#accessing the characters by index.
print(name[0]) #P, indexing starts from zero - access the first character.
print(name[1]) #a
print(name[2]) #l
print(name[3]) #a
print(name[4]) #k
print("\n")
# print(name[5]) #throws an error, since index five does not exist.

#negative indexing- accessing the characters from last.
#does not include 0 index.

print(name[-5]) #P
print(name[-4]) #a
print(name[-3]) #l
print(name[-2]) #a
print(name[-1]) #k

intro = """Hello!, this is Palak.
I'm learning python,
and it is so interesting."""
#accessing character in multi-line string with the help of loop.
for character in intro:
    print(character)
