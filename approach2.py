import numpy as np
import cv2
from matplotlib import pyplot as plt


def img():
    img = cv2.imread('scales.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
