from configparser import DuplicateOptionError
import numpy as np;
import cv2;

def getImage():
    return cv2.imread('paisaje.jpg')

def saveNewImg(img):
    cv2.imwrite("imagen-trasnformada.jpg", img)

def affineTransformImg():
    rows, cols, ch = image.shape
    pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
    pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.2], [cols * 0.1, rows * 0.9]])
    M = cv2.getAffineTransform(pts1, pts2)
    return cv2.warpAffine(image, M, (cols, rows))

def closeWindows():
    cv2.destroyAllWindows()

def init ():
    affineTransformImg()
    if key == ord('g'):
        saveNewImg(affineTransformationImg)
        closeWindows()
    else:
        closeWindows()

image = getImage()
affineTransformationImg = affineTransformImg()
cv2.imshow('Affine trasnformation', affineTransformationImg)
key = cv2.waitKey(0)
init()