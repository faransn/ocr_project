import numpy as np
import os
import string
import cv2
from PIL import Image, ImageFilter


def gaussian_noiser(file_path, dest_image, radius):
    image = Image.open(file_path)
    img = image
    if (radius != 0):
        filter = ImageFilter.GaussianBlur(radius)
        img = image.filter(filter)
    temp = string.replace(dest_image, ".jpg", "_" + str(radius) + "_" + ".jpg", 1)
    img.save(temp)


def guass_noisy(file_path, dest_image, mean, var):
    image = cv2.imread(file_path)
    row, col, ch = image.shape
    # mean = 0
    # var = 0.1
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    temp = string.replace(dest_image, ".jpg", "_" + str(mean) + "_" + str(var) + "_" + ".jpg", 1)
    cv2.imwrite(temp, noisy)


# rate = [(0, 0), (0, 0.1), (0, 0.2), (0, 0.3), (0.1, 0.1), (0.1, 0.2), (0.1, 0.3),
#         (0.3, 0.1), (0.3, 0.2), (0.3, 0.3), (0.5, 0.1), (0.5, 0.2), (0.5, 0.3), (1, 0.1), (1, 0.2), (1, 0.3)]

rate = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]


def coordinate(folder, dest, fixed):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            temp = string.replace(file_path, fixed, dest, 1)
            for m in rate:
                gaussian_noiser(file_path, temp, m)
        elif os.path.isdir(file_path):
            coordinate(file_path, dest, fixed)


folder = "Skewed/"
fixed = "Skewed"
dest = "Gaussian"
coordinate(folder, dest, fixed)
print "done!"


def noisy(noise_typ, image):
    if noise_typ == "gauss":
        row, col, ch = image.shape
        mean = 0
        var = 0.1
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        noisy = image + gauss
        return noisy
    elif noise_typ == "s&p":
        row, col, ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy
    elif noise_typ == "speckle":
        row, col, ch = image.shape
        gauss = np.random.randn(row, col, ch)
        gauss = gauss.reshape(row, col, ch)
        noisy = image + image * gauss
        return noisy
