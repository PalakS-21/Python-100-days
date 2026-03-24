
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
    ("2 + 2 ?", ("A. 3", "B. 6", "C. 5", "D. 4"), ("D")),
    ("Capital of India ?", ("A. Delhi", "B. Mumbai","C. Pune", "D. Jaipur" ), ("A")),
)

def start_quiz():
    score = 0
    total = len(quiz)

    i = 1

    for q in quiz:
        question, options, answer = q 

        print("\nQuestion", i)
        print(question)

        for opt in options:
            print(opt)

        user = input("Choose the correct options (A/B/C/D) : ").upper()

        if user == answer:
            print("Correct!✅")
            score += 1
        else:
            print("Wrong!❌, Correct answer :", answer)

        i += 1

    print("\nFinal Score:", score, "/", total) 

    percent = (score / total) * 100
    print(f"Percentage: {percent} % ")       

def main():
    while True:
        start_quiz()

        again = input('\nDo you want to retry ? (yes/no): ').lower()

        if again != "yes":       
            print("Goodbyee!!")
            break

main()