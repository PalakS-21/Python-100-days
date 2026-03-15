
# Guess the number game...in 5 attempts.

secret_num = 8
guessed = False

for i in range(5): 
    guess = int(input("Guess the secret number: "))

    if guess == secret_num:
        print("Woww!! You guessed it Correct 💪")
        break

    elif guess < secret_num:
        print("Too small. Try again 😁")

    else:
        print("Too big!! 😶")    



