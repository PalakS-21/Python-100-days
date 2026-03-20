
# to-do list app project

tasks = []

# add task
def add_task():
    task = input("Enter your tasks : ")
    tasks.append(task)
    print("Task added!")
    input("\nPress enter to continue...")

# remove task
def remove_task():
    task = input("Enter task to remove : ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed!")
        
    else:
        print("Task not found..")

# show task
def show_tasks():
    if not tasks:
        print("No task available : ")
    else:
        print("\nYour Tasks :")
        i = 1
        for t in tasks:           
            print(i, "-", t)
            i += 1

# Menu

while True:
    print("\n----------TO-DO MENU----------")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Task")
    print("4. Exit")

    choice = input("Enter choice :")

    if choice == '1':
        add_task()

    elif choice == '2':
        remove_task()

    elif choice == '3':
        show_tasks()

    elif choice == '4':
        print("Goodbyee 👋")    
        break

    else:
        print("Invalid choice!")