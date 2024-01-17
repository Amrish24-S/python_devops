def update_file(path, key, value):
    try:
        with open (path, 'r') as file:
            contents = file.readlines()
        with open (path, 'w') as file:
            for content in contents:
                if key in content:
                    file.write(key + "=" + value + "\n")
                else:
                    file.write(content)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")

update_file("server.conf", "MAX_CONNECTION", "1000")