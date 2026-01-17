# Write a python program to print the content of the directory using os module. 

import os

# Specify the directory path
directory_path = "."

# List and print directory contents
for item in os.listdir(directory_path):
    print(item)
