# Miscellaneous Python Scripts  
This Github repo is the collection of my all Python script that I write to automate any kind of job. I experienced that I write several useful automation scripts, but later I miss them because of unorganized storage. So, I decided to store all such useful Python scripts here in this repo.  
  
## 1. Resize all images  
I faced a problem while resizing all images in a directory, as it is a very tidy job. So, I thought to write a Python script for this and upload it on Github. To run this script:  
1. Save this script in your system with name `resize_images_script.py`.  
2. Pass the path of directory in which all the images are stored and the desired size of image, in the following way:  
`$ python resize_images_script.py path/to/directory/ 300`
This Python script will resize all the images inside path/to/directory/ to size 300xN, N would be decided by script so that it can preserve aspect ratio of image.  
  
OUTPUT:  
This Python script will resize all images and save it in the same directory with the same name.  
  
## 2. Spectrogram from WAV  
  

## 3. Librosa Audio Features  
  

## 4. Keypress Wait  
  

## 5. Generate GitIgnore  
  

## 6. Docker Project  
  

## 7. English Vocab  
  

## 8. Data Augmentation And Annotation  
This is a Python script to automate the data augmentation and annotation of images for Object Detection problems.  
This script helped me in annotating the object of interest for the data collected by myself.  
  
## 9. Click Coordinates  
This Python script will help to know the coordinates of any point on an image just by clicking there.  
This functionality will help in annotating the images for object detection use cases. To accomplish this, one has to click on the corners (generally top-left corner and bottom-right corner) of the object of interest and the script will print those coordinates on image as well as on terminal.  