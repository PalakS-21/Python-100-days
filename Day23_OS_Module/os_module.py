import os

# getcwd() -> Current Working Directory ("The folder where Python is currently running.")
print(os.getcwd())

# listdir() -> list all files and folders
print(os.listdir())

# chdir() -> change directory
os.chdir("Day23_OS_Module")
print(os.getcwd())

# mkdir() -> create a folder (only one folder)
# os.mkdir("Day23_OS_Module/Projects")

# makedirs()-> creates multiple folder
# os.makedirs("Day23_OS_Module/Projects/Beginner")

# rename folder -> rename()
# os.rename("Projects", "MiniProjects")

# print(os.listdir("MiniProjects"))

# emdir() -> delete empty folder, folder must be empty
# os.rmdir("MiniProjects") # if not empty -> OSError

# print(os.getcwd())

# check if file exists
print(os.path.exists("os_module.py"))

# check if folder exists
print(os.path.exists("Projects"))

# get absolute path
print(os.path.abspath("os_module.py"))

os.makedirs("Projects")
