
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