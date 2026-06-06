import os

# for i in range(1, 101):
#     folder = f"Day{i:02d}"

#     if not os.path.exists(folder):
#         os.rmdir(folder)

# print("100 folders deleted")


# deleting 100 folders (non-empty)

import stat

for i in range(1, 101):
    folder = f"Day{i:02d}"
    if os.path.exists(folder) and os.path.isdir(folder):
        # Remove read-only attribute if present
        os.chmod(folder, stat.S_IWRITE)

        # Delete only if empty
        if not os.listdir(folder):
            os.rmdir(folder)
            print(f"{folder} deleted")
        else:
            print(f"{folder} kept (not empty)")
