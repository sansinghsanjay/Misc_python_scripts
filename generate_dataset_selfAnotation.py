# packages
import os
import cv2
import random
import shutil
import numpy as np

# constants
CLASSNAME = "britanniacake"
CREATE_BB = False

# paths
orig_images_path = "C:/Users/sanjaysingh5/Documents/datasets/BrandRecognition/shopping_cart_experiment/Colgate/colgate_1-frames/"
dest_images_path = "C:/Users/sanjaysingh5/Documents/datasets/BrandRecognition/shopping_cart_experiment/Colgate/colgate_1-genFrames/"
dest_bb_path = "C:/Users/sanjaysingh5/Documents/datasets/BrandRecognition/shopping_cart_experiment/Colgate/colgate_1-genFrames_bb/"

# function to create bounding box around object of interest
def create_bounding_box(image, top_left, bottom_right):
    # mark bounding box in the image
    color = (255, 0, 0)
    thickness = 2
    image = cv2.rectangle(image, top_left, bottom_right, color, thickness)
    return image

# function to simply copy the image file
def simple_copy(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # mark bounding box
    if(CREATE_BB):
        image = create_bounding_box(image, top_left, bottom_right)
    # save image
    cv2.imwrite(dest_path + filename + "_simplecopy.jpg", image)
    # save bounding box
    to_write = classname + " 0 0 0 " + str(top_left[0]) + " " + str(top_left[1]) + " " + str(bottom_right[0]) + " " + str(bottom_right[1]) + " 0 0 0 0 0 0 0\n"
    f_ptr = open(dest_bb_path + filename + "_simplecopy.txt", "w")
    f_ptr.write(to_write)
    f_ptr.close()

# function to shift image left
def shift_left(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # find margins
    margin = top_left[0] - 0
    # generate 5 values (in percentage) to shift image towards left
    perc_shift = list()
    perc_shift.append(random.randint(15, 35))
    perc_shift.append(random.randint(35, 55))
    perc_shift.append(random.randint(55, 75))
    perc_shift.append(random.randint(75, 85))
    perc_shift.append(random.randint(85, 100))
    # convert shift position from percentage to absolute pixel values, shift image, and save it
    for i in range(len(perc_shift)):
        # get absolute shift value
        shift_margin = int((margin * perc_shift[i]) / float(100))
        # shift image (negate the value as we are shifting image towards left)
        M = np.float32([
            [1, 0, (-1) * shift_margin],
            [0, 1, 0]
        ])
        shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), borderMode=cv2.BORDER_WRAP)
        shifted_top_left = (top_left[0] - shift_margin, top_left[1])
        shifted_bottom_right = (bottom_right[0] - shift_margin, bottom_right[1])
        # create bounding box
        if(CREATE_BB):
            shifted_image = create_bounding_box(shifted_image, shifted_top_left, shifted_bottom_right)
        # save image
        cv2.imwrite(dest_path + filename + "_shiftleft_" + str(shift_margin) + ".jpg", shifted_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(shifted_top_left[0]) + " " + str(shifted_top_left[1]) + " " + str(shifted_bottom_right[0]) + " " + str(shifted_bottom_right[1]) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_shiftleft_" + str(shift_margin) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to shift image right
def shift_right(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # find margins
    margin = image.shape[1] - bottom_right[0]
    # generate 5 values (in percentage) to shift image towards left
    perc_shift = list()
    perc_shift.append(random.randint(15, 35))
    perc_shift.append(random.randint(35, 55))
    perc_shift.append(random.randint(55, 75))
    perc_shift.append(random.randint(75, 85))
    perc_shift.append(random.randint(85, 100))
    # convert shift position from percentage to absolute pixel values, shift image, and save it
    for i in range(len(perc_shift)):
        # get absolute shift value
        shift_margin = int((margin * perc_shift[i]) / float(100))
        # shift image (positive value of shift_margin as we are shifting image towards right)
        M = np.float32([
            [1, 0, shift_margin],
            [0, 1, 0]
        ])
        shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), borderMode=cv2.BORDER_WRAP)
        shifted_top_left = (top_left[0] + shift_margin, top_left[1])
        shifted_bottom_right = (bottom_right[0] + shift_margin, bottom_right[1])
        # create bounding box
        if(CREATE_BB):
            shifted_image = create_bounding_box(shifted_image, shifted_top_left, shifted_bottom_right)
        # save image
        cv2.imwrite(dest_path + filename + "_shiftright_" + str(shift_margin) + ".jpg", shifted_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(shifted_top_left[0]) + " " + str(shifted_top_left[1]) + " " + str(shifted_bottom_right[0]) + " " + str(shifted_bottom_right[1]) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_shiftright_" + str(shift_margin) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to shift image up
def shift_up(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # find margins
    margin = top_left[1] - 0
    # generate 5 values (in percentage) to shift image towards left
    perc_shift = list()
    perc_shift.append(random.randint(15, 35))
    perc_shift.append(random.randint(35, 55))
    perc_shift.append(random.randint(55, 75))
    perc_shift.append(random.randint(75, 85))
    perc_shift.append(random.randint(85, 100))
    # convert shift position from percentage to absolute pixel values, shift image, and save it
    for i in range(len(perc_shift)):
        # get absolute shift value
        shift_margin = int((margin * perc_shift[i]) / float(100))
        # shift image (negate the value of shift_margin as we are shifting image towards upward)
        M = np.float32([
            [1, 0, 0],
            [0, 1, (-1) * shift_margin]
        ])
        shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), borderMode=cv2.BORDER_WRAP)
        shifted_top_left = (top_left[0], top_left[1] - shift_margin)
        shifted_bottom_right = (bottom_right[0], bottom_right[1] - shift_margin)
        # create bounding box
        if(CREATE_BB):
            shifted_image = create_bounding_box(shifted_image, shifted_top_left, shifted_bottom_right)
        # save image
        cv2.imwrite(dest_path + filename + "_shiftup_" + str(shift_margin) + ".jpg", shifted_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(shifted_top_left[0]) + " " + str(shifted_top_left[1]) + " " + str(shifted_bottom_right[0]) + " " + str(shifted_bottom_right[1]) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_shiftup_" + str(shift_margin) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to shift image down
def shift_down(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # find margins
    margin = image.shape[0] - bottom_right[1]
    # generate 5 values (in percentage) to shift image towards left
    perc_shift = list()
    perc_shift.append(random.randint(15, 35))
    perc_shift.append(random.randint(35, 55))
    perc_shift.append(random.randint(55, 75))
    perc_shift.append(random.randint(75, 85))
    perc_shift.append(random.randint(85, 100))
    # convert shift position from percentage to absolute pixel values, shift image, and save it
    for i in range(len(perc_shift)):
        # get absolute shift value
        shift_margin = int((margin * perc_shift[i]) / float(100))
        # shift image (positive value of shift_margin as we are shifting image towards downward)
        M = np.float32([
            [1, 0, 0],
            [0, 1, shift_margin]
        ])
        shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), borderMode=cv2.BORDER_WRAP)
        shifted_top_left = (top_left[0], top_left[1] + shift_margin)
        shifted_bottom_right = (bottom_right[0], bottom_right[1] + shift_margin)
        # create bounding box
        if(CREATE_BB):
            shifted_image = create_bounding_box(shifted_image, shifted_top_left, shifted_bottom_right)
        # save image
        cv2.imwrite(dest_path + filename + "_shiftdown_" + str(shift_margin) + ".jpg", shifted_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(shifted_top_left[0]) + " " + str(shifted_top_left[1]) + " " + str(shifted_bottom_right[0]) + " " + str(shifted_bottom_right[1]) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_shiftdown_" + str(shift_margin) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to shift image towards top-left corner
def shift_topleft(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # find margins
    left_margin = top_left[0] - 0
    top_margin = top_left[1] - 0
    if(left_margin > top_margin):
        margin = top_margin
    else:
        margin = left_margin
    # generate 5 values (in percentage) to shift image towards left
    perc_shift = list()
    perc_shift.append(random.randint(15, 35))
    perc_shift.append(random.randint(35, 55))
    perc_shift.append(random.randint(55, 75))
    perc_shift.append(random.randint(75, 85))
    perc_shift.append(random.randint(85, 100))
    # convert shift position from percentage to absolute pixel values, shift image, and save it
    for i in range(len(perc_shift)):
        # get absolute shift value
        shift_left_margin = int((left_margin * perc_shift[i]) / float(100))
        shift_top_margin = int((top_margin * perc_shift[i]) / float(100))
        # shift image (negate the values of shift as we are shifting image towards top-left corner)
        M = np.float32([
            [1, 0, (-1) * shift_left_margin],
            [0, 1, (-1) * shift_top_margin]
        ])
        shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), borderMode=cv2.BORDER_WRAP)
        shifted_top_left = (top_left[0] - shift_left_margin, top_left[1] - shift_top_margin)
        shifted_bottom_right = (bottom_right[0] - shift_left_margin, bottom_right[1] - shift_top_margin)
        # create bounding box
        if(CREATE_BB):
            shifted_image = create_bounding_box(shifted_image, shifted_top_left, shifted_bottom_right)
        # save image
        cv2.imwrite(dest_path + filename + "_shifttopleft_" + str(shift_top_margin) + "_" + str(shift_left_margin) + ".jpg", shifted_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(shifted_top_left[0]) + " " + str(shifted_top_left[1]) + " " + str(shifted_bottom_right[0]) + " " + str(shifted_bottom_right[1]) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_shifttopleft_" + str(shift_top_margin) + "_" + str(shift_left_margin) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to shift image towards bottom-right corner
def shift_bottomright(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # find margins
    right_margin = image.shape[1] - bottom_right[0]
    bottom_margin = image.shape[0] - bottom_right[1]
    if(right_margin > bottom_margin):
        margin = bottom_margin
    else:
        margin = right_margin
    # generate 5 values (in percentage) to shift image towards left
    perc_shift = list()
    perc_shift.append(random.randint(15, 35))
    perc_shift.append(random.randint(35, 55))
    perc_shift.append(random.randint(55, 75))
    perc_shift.append(random.randint(75, 85))
    perc_shift.append(random.randint(85, 100))
    # convert shift position from percentage to absolute pixel values, shift image, and save it
    for i in range(len(perc_shift)):
        # get absolute shift value
        shift_right_margin = int((right_margin * perc_shift[i]) / float(100))
        shift_bottom_margin = int((bottom_margin * perc_shift[i]) / float(100))
        # shift image (keep positive values of shift as we are shifting image towards bottom-right corner)
        M = np.float32([
            [1, 0, shift_right_margin],
            [0, 1, shift_bottom_margin]
        ])
        shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), borderMode=cv2.BORDER_WRAP)
        shifted_top_left = (top_left[0] + shift_right_margin, top_left[1] + shift_bottom_margin)
        shifted_bottom_right = (bottom_right[0] + shift_right_margin, bottom_right[1] + shift_bottom_margin)
        # create bounding box
        if(CREATE_BB):
            shifted_image = create_bounding_box(shifted_image, shifted_top_left, shifted_bottom_right)
        # save image
        cv2.imwrite(dest_path + filename + "_shiftbottomright_" + str(shift_bottom_margin) + "_" + str(shift_right_margin) + ".jpg", shifted_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(shifted_top_left[0]) + " " + str(shifted_top_left[1]) + " " + str(shifted_bottom_right[0]) + " " + str(shifted_bottom_right[1]) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_shiftbottomright_" + str(shift_bottom_margin) + "_" + str(shift_right_margin) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to shift image towards top-right corner
def shift_topright(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # find margins
    right_margin = image.shape[1] - bottom_right[0]
    top_margin = top_left[1] - 0
    if(right_margin > top_margin):
        margin = top_margin
    else:
        margin = right_margin
    # generate 5 values (in percentage) to shift image towards left
    perc_shift = list()
    perc_shift.append(random.randint(15, 35))
    perc_shift.append(random.randint(35, 55))
    perc_shift.append(random.randint(55, 75))
    perc_shift.append(random.randint(75, 85))
    perc_shift.append(random.randint(85, 100))
    # convert shift position from percentage to absolute pixel values, shift image, and save it
    for i in range(len(perc_shift)):
        # get absolute shift value
        shift_right_margin = int((right_margin * perc_shift[i]) / float(100))
        shift_top_margin = int((top_margin * perc_shift[i]) / float(100))
        # shift image (negate top margin value of shift as we are shifting image towards top-right corner)
        M = np.float32([
            [1, 0, shift_right_margin],
            [0, 1, (-1) * shift_top_margin]
        ])
        shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), borderMode=cv2.BORDER_WRAP)
        shifted_top_left = (top_left[0] + shift_right_margin, top_left[1] - shift_top_margin)
        shifted_bottom_right = (bottom_right[0] + shift_right_margin, bottom_right[1] - shift_top_margin)
        # create bounding box
        if(CREATE_BB):
            shifted_image = create_bounding_box(shifted_image, shifted_top_left, shifted_bottom_right)
        # save image
        cv2.imwrite(dest_path + filename + "_shifttopright_" + str(shift_top_margin) + "_" + str(shift_right_margin) + ".jpg", shifted_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(shifted_top_left[0]) + " " + str(shifted_top_left[1]) + " " + str(shifted_bottom_right[0]) + " " + str(shifted_bottom_right[1]) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_shifttopright_" + str(shift_top_margin) + "_" + str(shift_right_margin) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to shift image towards bottom-left corner
def shift_bottomleft(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # find margins
    left_margin = top_left[0] - 0
    bottom_margin = image.shape[0] - bottom_right[1]
    if(left_margin > bottom_margin):
        margin = bottom_margin
    else:
        margin = left_margin
    # generate 5 values (in percentage) to shift image towards left
    perc_shift = list()
    perc_shift.append(random.randint(15, 35))
    perc_shift.append(random.randint(35, 55))
    perc_shift.append(random.randint(55, 75))
    perc_shift.append(random.randint(75, 85))
    perc_shift.append(random.randint(85, 100))
    # convert shift position from percentage to absolute pixel values, shift image, and save it
    for i in range(len(perc_shift)):
        # get absolute shift value
        shift_left_margin = int((left_margin * perc_shift[i]) / float(100))
        shift_bottom_margin = int((bottom_margin * perc_shift[i]) / float(100))
        # shift image (negate left margin value of shift as we are shifting image towards bottom-left corner)
        M = np.float32([
            [1, 0, (-1) * shift_left_margin],
            [0, 1, shift_bottom_margin]
        ])
        shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), borderMode=cv2.BORDER_WRAP)
        shifted_top_left = (top_left[0] - shift_left_margin, top_left[1] + shift_bottom_margin)
        shifted_bottom_right = (bottom_right[0] - shift_left_margin, bottom_right[1] + shift_bottom_margin)
        # create bounding box
        if(CREATE_BB):
            shifted_image = create_bounding_box(shifted_image, shifted_top_left, shifted_bottom_right)
        # save image
        cv2.imwrite(dest_path + filename + "_shiftbottomleft_" + str(shift_bottom_margin) + "_" + str(shift_left_margin) + ".jpg", shifted_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(shifted_top_left[0]) + " " + str(shifted_top_left[1]) + " " + str(shifted_bottom_right[0]) + " " + str(shifted_bottom_right[1]) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_shiftbottomleft_" + str(shift_bottom_margin) + "_" + str(shift_left_margin) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to resize the image
def zoom_resize_image(image, new_dim):
    resized_image = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)
    return resized_image

# function to calculate bounding box after resizing image
def zoom_new_bounding_box(top_left, bottom_right, actual_dim, resized_dim):
    # compute ratios
    rx = resized_dim[1] / float(actual_dim[1])
    ry = resized_dim[0] / float(actual_dim[0])
    # compute new coordinates of the bounding box
    new_top_left = (int(top_left[0] * rx), int(top_left[1] * ry))
    new_bottom_right = (int(bottom_right[0] * rx), int(bottom_right[1] * ry))
    # return new coordinates
    return new_top_left, new_bottom_right

# function to zoom-in
def zoom_in(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # get margin
    top_margin = top_left[1] - 0
    bottom_margin = image.shape[0] - bottom_right[1]
    left_margin = top_left[0] - 0
    right_margin = image.shape[1] - bottom_right[0]
    # find minimum of all the margins
    min_margin = top_margin
    if(min_margin > bottom_margin):
        min_margin = bottom_margin
    if(min_margin > left_margin):
        min_margin = left_margin
    if(min_margin > right_margin):
        min_margin = right_margin
    # zoom-in scale
    zoom_scale = int(min_margin / float(3))
    for i in range(3):
        # compute zoom margin
        if(i == 0):
            zoom_margin = int(zoom_scale * random.uniform(0.5, 1))
        else:
            zoom_margin = int(zoom_scale * random.uniform(i, (i + 1)))
        # compute crop coordinates for zooming
        zoom_x1 = top_left[0] - zoom_margin
        zoom_y1 = top_left[1] - zoom_margin
        zoom_x2 = bottom_right[0] + zoom_margin
        zoom_y2 = bottom_right[1] + zoom_margin
        # crop image for zoom-in
        zoom_image = image[zoom_y1 : zoom_y2, zoom_x1 : zoom_x2, :]
        # compute bounding box coordinates for zoomed image
        zoom_top_left = (zoom_margin, zoom_margin)
        zoom_bottom_right = (zoom_image.shape[1] - zoom_margin, zoom_image.shape[0] - zoom_margin)
        # resize image
        resized_image = zoom_resize_image(zoom_image, (image.shape[1], image.shape[0]))
        # get new coordinates of bounding box
        new_top_left, new_bottom_right = zoom_new_bounding_box(zoom_top_left, zoom_bottom_right, (zoom_image.shape[0], zoom_image.shape[1]), (resized_image.shape[0], resized_image.shape[1]))
        # mark bounding box
        if(CREATE_BB):
            resized_image = create_bounding_box(resized_image, new_top_left, new_bottom_right)
        # save image
        cv2.imwrite(dest_path + filename + "_zoomin_" + str(zoom_margin) + ".jpg", resized_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(new_top_left[0]) + " " + str(new_top_left[1]) + " " + str(new_bottom_right[0]) + " " + str(new_bottom_right[1]) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_zoomin_" + str(zoom_margin) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to zoom-out image
def zoom_out(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # zoom-out image at three zoom-out values
    for i in range(3):
        # create working copy of image
        work_image = np.copy(image)
        # randomly generate zoom-out value (in %)
        zoom_out_factor = random.uniform(0.4, 0.85)
        # compute new dimensions of image
        new_d1 = int(work_image.shape[0] * zoom_out_factor)
        new_d2 = int(work_image.shape[1] * zoom_out_factor)
        # resize image
        re_image = cv2.resize(work_image, (new_d2, new_d1))
        # randomly generate image blur kernel size
        blur_ksize = random.randint(30, 60)
        # blur the image
        work_image = cv2.blur(work_image, (blur_ksize, blur_ksize))
        # randomly generate coordinates to overlay the resized_image
        x_margin = work_image.shape[1] - re_image.shape[1]
        y_margin = work_image.shape[0] - re_image.shape[0]
        x1 = random.randint(0, x_margin)
        y1 = random.randint(0, y_margin)
        # overlay resize image on blurred image        
        work_image[y1 : (y1 + re_image.shape[0]), x1 : (x1 + re_image.shape[1]), :] = re_image
        # get new coordinates of bounding box
        new_top_left, new_bottom_right = zoom_new_bounding_box(top_left, bottom_right, (work_image.shape[0], work_image.shape[1]), (re_image.shape[0], re_image.shape[1]))
        new_top_left = (new_top_left[0] + x1, new_top_left[1] + y1)
        new_bottom_right = (new_bottom_right[0] + x1, new_bottom_right[1] + y1)
        # mark bounding box
        if(CREATE_BB):
            work_image = create_bounding_box(work_image, new_top_left, new_bottom_right)
        # save overlay image
        cv2.imwrite(dest_path + filename + "_zoomout_" + str(int(zoom_out_factor * 100)) + ".jpg", work_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(new_top_left[0]) + " " + str(new_top_left[1]) + " " + str(new_bottom_right[0]) + " " + str(new_bottom_right[1]) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_zoomout_" + str(int(zoom_out_factor * 100)) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to calculate new coordinates after rotation
def coords_after_rotation(x, y, p, q, angle):
    x_new = int(((x - p) * np.cos(angle)) - ((y - q) * np.sin(angle)) + p)
    y_new = int(((x - p) * np.sin(angle)) + ((y - q) * np.cos(angle)) + q)
    return x_new, y_new

# function to find the range of rotation so that object of interest doesn't get cut
def find_angle_range(width, height, x1, y1, x2, y2, p, q):
    # to store maximum and minimum angle
    rot_angle = 0
    # find angle
    for i in range(5, 180, 5):
        # pass flag
        consider_angle = True
        # convert angle into radians (towards positive side)
        angle_rad = np.radians(i)
        # get new coordinates
        x1_new, y1_new = coords_after_rotation(x1, y1, p, q, angle_rad)
        x2_new, y2_new = coords_after_rotation(x2, y1, p, q, angle_rad)
        x3_new, y3_new = coords_after_rotation(x2, y2, p, q, angle_rad)
        x4_new, y4_new = coords_after_rotation(x1, y2, p, q, angle_rad)
        # check if new coordinates are in range or not
        if(x1_new < 0 or x1_new > width):
            consider_angle = False
        if((y1_new < 0 or y1_new > height) and consider_angle == True):
            consider_angle = False
        if((x2_new < 0 or x2_new > width) and consider_angle == True):
            consider_angle = False
        if((y2_new < 0 or y2_new > height) and consider_angle == True):
            consider_angle = False
        if((x3_new < 0 or x3_new > width) and consider_angle == True):
            consider_angle = False
        if((y3_new < 0 or y3_new > height) and consider_angle == True):
            consider_angle = False
        if((x4_new < 0 or x4_new > width) and consider_angle == True):
            consider_angle = False
        if((y4_new < 0 or y4_new > height) and consider_angle == True):
            consider_angle = False
        if(consider_angle == False):
            break
        else:
            rot_angle = i
    # return min and max angle of rotation
    return rot_angle

# function to rotate image
def rotate_image(classname, imagename, source_path, dest_path, dest_bb_path, top_left, bottom_right):
    # get filename
    filename = imagename.split(".")[0]
    # read image
    image = cv2.imread(source_path + imagename)
    # get coords of bounding box
    x1 = top_left[0]
    y1 = top_left[1]
    x2 = bottom_right[0]
    y2 = bottom_right[1]
    # find point of rotation
    p = int((x1 + x2) / 2.0)
    q = int((y1 + y2) / 2.0)
    # get maximum angle of rotation (max and min)
    max_angle = find_angle_range(image.shape[1], image.shape[0], x1, y1, x2, y2, p, q)
    # make three rotations in clockwise and three rotations in anti-clockwise
    for i in range(6):
        # create working copy of image
        work_image = np.copy(image)
        # randomly generate angle of rotation (in degrees)
        rot_angle = random.randint(0, max_angle)
        # rotation will be clockwise if i is even, otherwise anti-clockwise
        if((i % 2) != 0):
            rot_angle = (-1) * rot_angle
        # convert max_angle into radians
        angle_rad = np.radians(rot_angle)
        # find new coordinates of the bounding box after rotation
        x1_new, y1_new = coords_after_rotation(x1, y1, p, q, angle_rad)
        x2_new, y2_new = coords_after_rotation(x2, y1, p, q, angle_rad)
        x3_new, y3_new = coords_after_rotation(x2, y2, p, q, angle_rad)
        x4_new, y4_new = coords_after_rotation(x1, y2, p, q, angle_rad)
        # get rotation matrix
        M = cv2.getRotationMatrix2D((p, q), (-1) * rot_angle, 1)
        # rotate image
        work_image = cv2.warpAffine(work_image, M, (work_image.shape[1], work_image.shape[0]))
        # finding bounding box coordinates
        x1_mark = np.min([x1_new, x2_new, x3_new, x4_new])
        x2_mark = np.max([x1_new, x2_new, x3_new, x4_new])
        y1_mark = np.min([y1_new, y2_new, y3_new, y4_new])
        y2_mark = np.max([y1_new, y2_new, y3_new, y4_new])
        # mark bounding box
        if(CREATE_BB):
            work_image = create_bounding_box(work_image, (x1_mark, y1_mark), (x2_mark, y2_mark))
        # save image
        cv2.imwrite(dest_path + filename + "_rotation_" + str(rot_angle) + ".jpg", work_image)
        # save bounding box
        to_write = classname + " 0 0 0 " + str(x1_mark) + " " + str(y1_mark) + " " + str(x2_mark) + " " + str(y2_mark) + " 0 0 0 0 0 0 0\n"
        f_ptr = open(dest_bb_path + filename + "_rotation_" + str(rot_angle) + ".txt", "w")
        f_ptr.write(to_write)
        f_ptr.close()

# function to extract coordinates of bounding box
def extract_bb_coords(filename):
    top_left = list()
    bottom_right = list()
    f_ptr = open(filename, "r")
    data = f_ptr.read()
    f_ptr.close()
    lines = data.split("\n")
    for line in lines:
        if(len(line) > 1):
            splits = line.split(" ")
            top_left.append(int(splits[4]))
            top_left.append(int(splits[5]))
            bottom_right.append(int(splits[6]))
            bottom_right.append(int(splits[7]))
    return top_left, bottom_right

# get list of all imags
images_list = os.listdir(orig_images_path)

# name of annotation txt file
annotationFile = ""
for i in range(len(images_list)):
    imagename = images_list[i]
    splits = imagename.split(".")
    if(splits[len(splits) - 1] == "txt"):
        annotationFile = imagename
        images_list.remove(imagename)
        break

# remove anotation file from the images list
'''
annotation_files = list()
for i in range(len(images_list)):
    imagename = images_list[i]
    splits = imagename.split(".")
    if(splits[len(splits) - 1] == "txt"):
        annotation_files.append(imagename)
for i in range(len(annotation_files)):
    images_list.remove(annotation_files[i])
'''
# extract coordinates
top_left = list()
bottom_right = list()
f_ptr = open(orig_images_path + annotationFile, "r")
data = f_ptr.read()
f_ptr.close()
lines = data.split("\n")
for line in lines:
    if(len(line) > 1):
        splits = line.split(" ")
        if(len(top_left) == 0):
            top_left.append(int(splits[0]))
            top_left.append(int(splits[1]))
        else:
            bottom_right.append(int(splits[0]))
            bottom_right.append(int(splits[1]))

# process each image file
for i in range(len(images_list)):
    # get coordinates of the bounding box
    #coord_filename = images_list[i].split(".")[0] + ".txt"
    #top_left, bottom_right = extract_bb_coords(orig_images_path + coord_filename)
    # apply simple copy
    simple_copy(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply shift left
    shift_left(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply shift right
    shift_right(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply shift up
    shift_up(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply shift down
    shift_down(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply shift top-left
    shift_topleft(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply shift bottom-right
    shift_bottomright(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply shift top-right
    shift_topright(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply shift bottom-left
    shift_bottomleft(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply zoom-in
    zoom_in(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply zoom-out
    zoom_out(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
    # apply rotation
    rotate_image(CLASSNAME, images_list[i], orig_images_path, dest_images_path, dest_bb_path, top_left, bottom_right)
print("All images processed and saved with their annotation details successfully")
