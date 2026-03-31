# phonebook

# creating an empty dictionary : phonebook = {}

phonebook = {}

# Design Menu

while True:
    print("\n1. Add Contacts")
    print("\n2. Search Contact")
    print("\n3. Show all")
    print("\n4. Delete Contact")
    print("\n5. Exit \n")

    choice  = input("Enter your choice : ")

    if choice == '1':
        name = input("Add Contact :")
        number = int(input("Enter Contact Number :"))
        phonebook[name] = number
        print("Contact saved successfully!")

    elif choice == '2':
        name = input("Enter name to search :")
        print(phonebook.get(name, "Not found"))

    elif choice == '3':
        for name, number in phonebook.items():
            print(name, ":", number)    

    elif choice == '4':
        name = input("Enter name to delete :")

        if name in phonebook:
            phonebook.pop(name)     
            print("Deleted Successfully!")
        else:
            print("Contact not Found!")

    elif choice == '5':
        break

    else:
        print("Invalid Choice")        