# packages
import cv2
import os

# paths
image_path = "C:/Users/sanjaysingh5/Documents/datasets/BrandRecognition/shopping_cart_experiment/Cocacola/cocacola_v1-frames/cocacola_1-0001.jpg"
all_images_path = "C:/Users/sanjaysingh5/Documents/datasets/BrandRecognition/shopping_cart_experiment/Cocacola/cocacola_v1-frames/"

# variables to store coordinates
top_left = list()
bottom_right = list()

# function to display the coordinates of
# of the points clicked on the image 
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        if(len(top_left) == 0):
            top_left.append(x)
            top_left.append(y)
        else:
            bottom_right.append(x)
            bottom_right.append(y)
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(re_image, str(x) + ',' + str(y), (x,y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', re_image)
    # checking for right mouse clicks     
    if event==cv2.EVENT_RBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = re_image[y, x, 0]
        g = re_image[y, x, 1]
        r = re_image[y, x, 2]
        cv2.putText(re_image, str(b) + ',' + str(g) + ',' + str(r), (x,y), font, 1, (255, 255, 0), 2)
        cv2.imshow('image', re_image)

# read image
image = cv2.imread(image_path)

# get dimension
r = 512.0 / image.shape[1]
dim = (512, int(image.shape[0] * r))

# resize image
re_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# show image
cv2.imshow("image", re_image)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

# make path for text file
splits = image_path.split("/")
filename = splits[len(splits) - 1].split(".")[0]
splits = splits[:len(splits) - 1]
txt_path = "/".join(splits) + "/" + filename + "_bbAnotations.txt"

# write bounding box coordinates
f_ptr = open(txt_path, "w")
to_write = str(top_left[0]) + " " + str(top_left[1]) + "\n"
to_write += str(bottom_right[0]) + " " + str(bottom_right[1])
f_ptr.write(to_write)
f_ptr.close()
print("Annotation information saved successfully")

# get all images
images_list = os.listdir(all_images_path)

# resize each image
for i in range(len(images_list)):
    # get filename and its extension
    splits = images_list[i].split(".")
    filename = splits[0]
    ext = splits[1]
    if(ext != "txt"):
        # read image
        image = cv2.imread(all_images_path + images_list[i])
        # resize image
        re_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        # save resized image
        cv2.imwrite(all_images_path + images_list[i], re_image)
print("Resized all images successfully")
