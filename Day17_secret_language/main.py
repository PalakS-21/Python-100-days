# importing encoder and decoder in main.py

from encoder import encode
from decoder import decode

print("---Secret Language Encoder and Decdoder---")

choice = input("Type 'e' to encode or 'd' to decode: ").lower()

word = input("Enter word: ")

if choice == 'e':

    result = encode(word)
    print("Encoded word: ", result)

elif choice == 'd':

    result = decode(word)
    print("Decoded word: ", result)

else:
    print("Invalid chouice!")