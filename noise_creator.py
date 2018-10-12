# -*- coding: utf-8 -*-
import cv2
import os
import config
from sp_noise import sp_noise


def noise_creator(source_img_folder):

    source_dir = "./" + config.image_folder + source_img_folder
    destination_dir = config.image_folder + config.main_sp_noise_folder + source_img_folder + "/"
    directory_files = os.listdir(source_dir)
    for i in range(0, len(directory_files)):
        source_image = cv2.imread(source_dir + "/" + str(directory_files[i]), 0)
        noise_image = sp_noise(source_image, 0.03)
        cv2.imwrite(
            destination_dir + os.path.splitext(directory_files[i])[0] + config.image_format, noise_image)
