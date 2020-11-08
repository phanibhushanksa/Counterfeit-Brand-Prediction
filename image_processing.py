
# Common imports
import numpy as np
import os
import pandas as pd
from pathlib import Path
from PIL import Image
import os, shutil
from os import listdir
import PIL
from PIL import Image
from matplotlib import pyplot
import scipy

# image = np.asarray(PIL.Image.open('image_name.jpg'))
# print(image)
# # display_image = Image.fromarray(image)
# # pyplot.imshow(display_image)
# pyplot.show()

# test_images=[image]
# test_images_list =[0] * len(test_images) 
# for i in range(0,len(test_images)):
#     test_images_list[i] = np.reshape((test_images[i]),(400,300,1))
# test = np.asarray(test_images_list)
# test = test.astype('float32')
# test /= 255

# print(test)
# Method to convert a 3D RGB image to 2D gray scale image
from scipy import average
import requests

def download_image(image_url):
    img_data = requests.get(image_url).content
    with open('static/images/image_name.jpg', 'wb') as handler:
        handler.write(img_data)

def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

## Method to load images and add to a numpy array
def load_images_to_np_array(fname):
    images_dir = Path('static/images').expanduser()
    dim = (400, 300)
    # Resizing all the images to same dimension
    images = []
    fpath = os.path.join(images_dir, fname)
    im = Image.open(fpath)
    im_resized = im.resize(dim)
    images.append(im_resized)

    ## Converting the image to numpy array
    images_arr=[]
    for x in range(len(images)):
        image=np.array(images[x])
        image = to_grayscale(image)
        images_arr.append(image)
    return images_arr

def get_x_value(image_name):
    test_images = load_images_to_np_array(image_name)
    test_images_list =[0] * len(test_images) 
    for i in range(0,len(test_images)):
        test_images_list[i] = np.reshape((test_images[i]),(400,300,1))
    test = np.asarray(test_images_list)
    test = test.astype('float32')
    test /= 255
    return test

