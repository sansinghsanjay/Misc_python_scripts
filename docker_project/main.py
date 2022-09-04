# packages
import os
import sys

# function to replace backward slashes by forward slashes
def process_path(path):
	path = path.replace("\\", "/")
	path = path.strip()
	return path

# check if path exists or not
def is_path_exists(path):
	if(os.path.exists(path) == True):
		return True
	else:
		return False

# get number of command line arguments
nbr_args = len(sys.argv)

# if number of command line arguments are not 1, then terminate the program
if(nbr_args != 1):
	print("Number of arguments is not 1. Exiting...")
	sys.exit(0)

# welcome
print("Hello to the beautiful and powerful world of Python...")

# get path from user
path = sys.argv[0]

# process path
path = process_path(path)

# check if path is valid
if(is_path_exists(path) == True):
	print("Congratulations, path exists!")
else:
	print("Oh.. path doesn't exists, exiting...")
	sys.exit(0)

# get files from that path
files = os.listdir(path)

# print the content
print("Total number of files and / or sub-directories: ", len(files))
print("Following are the files and / or sub-directories:")
for i in range(len(files)):
	print(files[i])
