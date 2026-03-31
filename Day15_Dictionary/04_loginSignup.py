# Login + SignuP System

users = {}

while True:
    print("\n1. Signup")
    print("\n2. Login")
    print("\n3. Change Password")
    print("\n4. Delete Account")
    print("\n5. Show Users")
    print("\n6. Exit")

    choice = input("\nPlease enter your choice :")

    # SIGNUP
    if choice == '1':
        username = input("\nEnter Username :").lower()
        password = input("Enter password :")

        if username in users:
            print("User already exists. Please Login")
        else:
            users[username] = password
            print("Signup Succesful")

    # LOGIN with limited attempts
    elif choice == '2':
        username = input("Enter Username :").lower()

        if username not in users:
            print("User not found")
        else:
            attempts = 3

            while attempts > 0:
                password = input("Enter password  :")

                if users[username] == password:
                    print("Login Successful.")
                    break
                else:
                    attempts -= 1
                    print("Wrong password. Attempts left :", attempts)

            if attempts == 0:
                print("Account locked (too manyu incorrect attempts.)")

    # CHANGE PASSWORD
    elif choice == '3':
        username = input("Enter Username :").lower()

        if username in users : 
            old_password = input("Enter old password :") 
             
            if users[username] == old_password:
                new_password = input("Enter new password :")
                users[username] = new_password
                print("Password changed successfully.")
            else:
                print("Wrong password")
        else:
            print("User not found.")  

    # DELETE ACCOUNT
    elif choice == '4':
        username = input("Enter Username :").lower()

        if username in users:
            confirm = print("Are you sure you want to delete your Account ? (yes/no) :")

            if confirm.lower() == 'yes':
                users.pop(username)
                print("Account Deleted Successfully.")

            else:
                print("Cancelled.")

        else:
            print("User not found")


    # SHOW USERS
    elif choice == '5':
        for user in users:
            print(user)                             

    # EXIT
    elif choice == '6':
        break

    else:
        print("Invalid choice. Try Again.")
