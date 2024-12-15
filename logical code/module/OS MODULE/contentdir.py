import os

# Specify the path of the directory you want to list
directory_path = "D:/ALLCODE/python/logical code/module"

# List the contents of the directory
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)
