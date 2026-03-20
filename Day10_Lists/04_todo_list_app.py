
# to-do list app project

tasks = []

# add task
def add_task():
    task = input("Enter your tasks : ")
    tasks.append(task)
    print("Task added!")

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