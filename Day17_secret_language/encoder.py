# encoding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
#  simply reverse the string

word = input("Enter a word :")

if len(word) >= 3:

    secret = "xyz" + word[1:] + word[0] + "abc"
    # ex : word = harry
    # word[1:] -> arry
    # word[1:] + word[0] -> arry + h -> arryh

    print("Encoded word:", secret)

else:
    print("Encoded word:", word[::-1])

    # word[::-1] -> yrrah (reversed)