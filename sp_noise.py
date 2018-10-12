# -*- coding: utf-8 -*-
import numpy as np
import random


'''
Add salt and pepper noise to image
prob: Probability of the noise
'''


# Salt and pepper noise
def sp_noise(source_image, prob):

    output = np.zeros(source_image.shape, np.uint8)
    thres = 1 - prob 
    for i in range(source_image.shape[0]):
        for j in range(source_image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = source_image[i][j]
    return output

