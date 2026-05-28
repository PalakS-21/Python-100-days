# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#  remove 3 characters from start and end. Now remove the last letter and dappend it to the beginning.

word = input("Enter the encoded word :")

if len(word) >= 3:

    temp = word[3:-3] # [start:end]

    normal = temp[-1] + temp[:-1]
    # temp[-1] -> last character
    # temp[:-1] -> not including the last character

    print("Decoded word :", normal)

else:
    print(word[::-1])