# Miscellaneous Python Scripts

This Github repo is the collection of my all Python script that I write to automate any kind of job. I experienced that I write several useful automation scripts, but later I miss them because of unorganized storage. So, I decided to store all such useful Python scripts here in this repo.

## 1. Resize all images in a directory
I faced a problem while resizing all images in a directory, as it is a very tidy job. So, I thought to write a Python script for this and upload it on Github. To run this script:
1. Save this script in your system with name "resize_images_script.py".
2. Pass the path of directory in which all the images are stored and the desired size of image, in the following way: 
$ python resize_images_script.py path/to/directory/ 300
This Python script will resize all the images inside path/to/directory/ to size 300xN, N would be decided by script so that it can preserve aspect ratio of image.

OUTPUT:
This Python script will resize all images and save it in the same directory with the same name.
