import re
file_Path = 'a:/Vagrantfile'
pattern = r"memory"

try:
    with open (file_Path, 'r') as file:
        file_content = file.read()
        match = re.search(pattern, file_content)
        if match:
            print("Match found")
        else:
            print("Not found")
except FileNotFoundError:
    print("File not found") 