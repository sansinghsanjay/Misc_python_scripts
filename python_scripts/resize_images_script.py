# libraries
import os
import sys
import cv2

# global consts
NUMBER_ARGS = 3

# vars
image_path = ""
image_size_x = 0
image_size_y = 0

# check number of command line argv
if(len(sys.argv) != NUMBER_ARGS):
	print("XXX Error: Invalid number of command line argv XXX")
	sys.exit(0)

# get image path from command line argv
image_path = sys.argv[1]
if(os.path.exists(image_path) == False):
	print("XXX Error: Path not found XXX")
	sys.exit(0)

# resolving '/' issue in image_path
if(image_path[len(image_path) - 1] != '/'):
	image_path = image_path + '/'

# get image size
image_size_x = int(sys.argv[2])

# get list of all image files
image_files = os.listdir(image_path)

# read all images, resize them and save them with the same name
for i in range(len(image_files)):
	# read image
	image = cv2.imread(image_path + image_files[i])
	# get image size
	image_size = image.shape
	# calculate image_size_y
	image_size_y = int(image_size_x * (image_size[1] / float(image_size[0])))
	# resize image
	image = cv2.resize(image, (image_size_x, image_size_y))
	# save image with the same name
	cv2.imwrite(image_path + image_files[i], image)
	# update status
	if(i % 1000 == 0):
		print("Done with ", i + 1, " of ", len(image_files))
	if(i == len(image_files) - 1):
		print("Done with ", i + 1, " of ", len(image_files))
print("JOB DONE SUCCESSFULLY")
