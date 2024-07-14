import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('m02ex01_image_and_tabular_data/data/dog.jpeg')

def lightness(vector):
    return (max(vector) + min(vector)) / 2

def average(vector):
    return vector.mean()

def luminosity(vector):
    return 0.21*vector[0] + 0.72*vector[1] + 0.07*vector[2]

gray_img_01 = np.apply_along_axis(lightness, axis=2, arr=img)
print(gray_img_01[0, 0])

gray_img_02 = np.apply_along_axis(average, axis=2, arr=img)
print(gray_img_02[0, 0])

gray_img_03 = np.apply_along_axis(luminosity, axis=2, arr=img)
print(gray_img_03[0, 0])