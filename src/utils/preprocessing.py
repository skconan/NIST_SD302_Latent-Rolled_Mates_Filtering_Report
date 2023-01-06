import cv2 as cv
import numpy as np


def contrast_enhancement(img):
    img = img / 255.
    smoothed_img = cv.blur(img, (15, 15))
    sign_img = img - smoothed_img
    sign_img[sign_img > 0] = 1
    sign_img[sign_img <= 0] = -1

    enhanced_img = sign_img * np.log(1+np.abs(img - smoothed_img))

    return enhanced_img


def flat_field_correction(img, ksize=61):
    dst = cv.GaussianBlur(img, (ksize, ksize), 0)
    corrected = np.uint8((img/dst)*dst.mean())
    return corrected


def clahe(img):
    rows, cols = img.shape[:2]
    clahe = cv.createCLAHE(clipLimit=8, tileGridSize=(rows//64, cols//64))
    img_clahe = clahe.apply(img)
    return img_clahe
