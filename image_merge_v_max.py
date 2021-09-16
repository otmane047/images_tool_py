# define a function for vertically 
# concatenating images of different
# widths
import os
import cv2
import itertools


path = '.'


def get_img_list():
    images = []
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            i = cv2.imread(os.path.join(path, file))
            images.append(i)
            
    itertools.groupby(files, keyfunc)
    return images


def vconcat_resize(img_list, interpolation=cv2.INTER_CUBIC):
    # take minimum width
    w_max = max(img.shape[1]
                for img in img_list)
    # resizing images
    im_list_resize = [cv2.resize(img,
                                 (w_max, int(img.shape[0] * w_max / img.shape[1])),
                                 interpolation=interpolation)
                      for img in img_list]
    # return final image
    return cv2.vconcat(im_list_resize)

splited_image_list = get_img_list().
# function calling
img_v_resize = vconcat_resize(get_img_list())
# show the output image

cv2.imshow('merged_image.jpg', img_v_resize)
cv2.imwrite('merged_image.jpg', img_v_resize)

