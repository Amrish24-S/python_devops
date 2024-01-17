import os
folders = input("Enter the folders (with space in between to differenciate): ").split()
print("\n")
for folder in folders:
    try:
        files = os.listdir(folder)
        print(f"Files in {folder}")
        for file in files:
            print(file)
        print("\n")
    except FileNotFoundError:
        print(f"Check the folder name: {folder}")
    except PermissionError:
        print("You dont have the permission to access the folder")
