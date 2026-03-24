
# bus seat booking view, where seat are fixed.

seats = ("A1", "A2", "A3", "A4")

def show_seats():
    for seat in seats:
        print("Seat :", seat)

show_seats()        

# product catalog

products = (
    ("Shoes", 799),
    ("T-shirts", 459),
    ("Bag", 799)
)
def show_products():
    for p in products:
        name, price  = p
        print(name, "-> $", price)

show_products()        

# Quiz App

quiz = (
    ("2 + 2 ?", "4"),
    ("Capital of India ?", "Delhi"),
    ("5 * 2 ?", "10")
)

def start_quiz():
    score = 0

    for q in quiz:
        question, answer = q 
        user = input(question + " ")

        if user.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("Your Score : ", score)        

start_quiz()        