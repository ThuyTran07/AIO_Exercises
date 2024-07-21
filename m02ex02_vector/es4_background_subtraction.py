import numpy as np
import cv2

def compute_difference(bg_img, ob_img):
    diff_img = cv2.absdiff(ob_img, bg_img)
    return diff_img

def compute_binary_mask(diff_img):
    _, mask_img = cv2.threshold(diff_img, 10, 255, cv2.THRESH_BINARY)
    return mask_img

def replace_background(new_bg_img, ob_img, bg_img):
    diff_img = compute_difference(bg_img, ob_img)
    mask_img = compute_binary_mask(diff_img)
    output = np.where(mask_img == 255, ob_img, new_bg_img)
    return output

#1 - Read & resize images
bg_img = cv2.imread('m02ex02_vector/data/GreenBackground.png')
bg_img = cv2.resize(bg_img, (678, 381))

ob_img = cv2.imread('m02ex02_vector/data/Object.png')
ob_img = cv2.resize(ob_img, (678, 381))

new_bg_img = cv2.imread('m02ex02_vector/data/NewBackground.jpg')
new_bg_img = cv2.resize(new_bg_img, (678, 381))

new_img = replace_background(new_bg_img, ob_img, bg_img)

cv2.imwrite('m02ex02_vector/data/Output.png', new_img)
