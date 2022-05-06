import numpy as np;
import cv2;

def getImage():
    return cv2.imread('paisaje.jpg')

def saveNewImg(img):
    cv2.imwrite("imagen-rotada.jpg", img)

def rotate(img, angle, center=None, scale=1.0):
    (height, width) = (img.shape[:2])

    if center is None:
        center = (width/2, height/2)

    matrix = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(img, matrix, (width, height))

def traslate(img, x, y):
    (height, width) = (img.shape[0], img.shape[1])
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img, matrix, (width, height))

def euclideanTransformation(img, angle, xTraslation, yTraslation):
    rotated = rotate(img, angle)
    return traslate(rotated, xTraslation, yTraslation)

def closeWindows():
    cv2.destroyAllWindows()

def init ():
    if key == ord('g'):
        saveNewImg(euclideanImg)
        closeWindows()
    else:
        closeWindows()

image = getImage()
euclideanImg = euclideanTransformation(image, -60, 25, 30)
cv2.imshow('image', euclideanImg)
key = cv2.waitKey(0)
init()
