import os

def files_in_Folder(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "File not Found"
    except PermissionError:
        return None, "Permission Denied"

def main():
    folders = input("Enter the folder name (with space inBetween): ").split()
    for folder in folders:
        files, errormsg = files_in_Folder(folder)
        if files:
            print(f"Files in {folder}")
            for file in files:
                print(file)
        else:
            print(errormsg)
        print("\n")
if __name__ == "__main__":
    main()