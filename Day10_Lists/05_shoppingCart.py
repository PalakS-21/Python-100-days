# Shopping cart mini project

cart = []
def add_to_cart():
    item = input("Enter item : ")
    cart.append(item)
    print("Item added to Cart!!")

def remove_item():
    item = input("Enter item to  remove: ")
    if item in cart:
        cart.remove(item)
        print("Item removed!")
    else:
        print("Item not found!")

def show_cart():
    print("Cart items : ", cart)

while True:
    print("\n1. Add\n2. Remove\n3. Show\n4. Exit")
    ch = input("Choice : ")

    if ch == '1':
        add_to_cart()

    elif ch == '2':
        remove_item()

    elif ch == '3':
        show_cart()

    elif ch == '4':
        break 