# packages
import os
import sys

# global variables
dir_list = list()
ignore_list = list()
file_ext_list = list()

# constants
SIZE_LIMIT = 99.5 # (in MBs)

# function to convert file size into MBs
def get_MB(filesize):
	kb = filesize/float(1024)
	mb = kb / float(1024)
	return mb

# function to check for directory and files; prepare ignore_list
def search_fun(path):
	# access global variables
	global dir_list, ignore_list, file_ext_list
	# get content
	temp_list = os.listdir(path)
	# check the content - if it is a directory or not
	for i in range(len(temp_list)):
		current_path = path + temp_list[i]
		# if directory then add it in the dir_list
		if(os.path.isdir(current_path) == True):
			current_path = current_path + "/"
			dir_list.append(current_path)
		else:
			# else (it is a file) if it is in extension list then put it in ignore list
			splits = temp_list[i].split(".")
			if((splits[len(splits) - 1].upper() in file_ext_list) or (splits[len(splits) - 1].lower() in file_ext_list)):
				ignore_list.append(current_path)
			# check if the size of file is more than SIZE_LIMIT (in MBs)
			if(get_MB(os.path.getsize(current_path)) > SIZE_LIMIT):
				ignore_list.append(current_path)

# get paths
search_path = input("Enter search path (without any quotes): ")

# replace all back-slashes with forward-slashes
search_path = search_path.replace("\\", "/")

# put a forward-slash at the end if it is not there
if(search_path[len(search_path) - 1] != "/"):
	search_path = search_path + "/"

# check if path exists or not
if(os.path.exists(search_path) == False):
	print("Entered path doesn't exists. Terminating script...")
	sys.exit(0)

# git gitignore path
gitignore_path = input("Enter path of gitignore (without any quotes, only up to directory name): ")

# replace all back-slashes with forward-slashes
gitignore_path = gitignore_path.replace("\\", "/")

# put a forward-slash at the end if it is not there
if(gitignore_path[len(gitignore_path) - 1] != "/"):
	gitignore_path = gitignore_path + "/"

# check if path exists or not
if(os.path.exists(gitignore_path) == False):
	print("Entered path doesn't exists. Terminating script...")
	sys.exit(0)

# get file extensions to be excluded
file_extensions = input("Enter comma separated list of file extensions (without dot) that needs to be excluded OR press enter if nothing needs to be excluded: ")

# create list of file extensions that needs to be excluded
if(len(file_extensions) > 0):
	temp_list = file_extensions.split(",")
	for i in range(len(temp_list)):
		file_ext_list.append(temp_list[i].strip())

# iterating all directories and sub-directories
dir_list.append(search_path)
i_ptr = 0
while(i_ptr < len(dir_list)):
	search_fun(dir_list[i_ptr])
	i_ptr = i_ptr + 1

# writing gitignore list items in gitignore file
f_ptr = open(gitignore_path + ".gitignore", "w")
gitignore_text = ''
for item in ignore_list:
	gitignore_text = gitignore_text + item + "\n"
f_ptr.write(gitignore_text)
f_ptr.close()
print(".gitignore created successfully")