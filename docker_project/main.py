# packages
import os

# welcome
print("Hello to the beautiful and powerful world of Python...")

# get path from user
path = input("Enter path: ")

# get files from that path
files = os.listdir(path)

# print the content
print("Total number of files and / or sub-directories: ", len(files))
print("Following are the files and / or sub-directories:")
for i in range(len(files)):
	print(files[i])