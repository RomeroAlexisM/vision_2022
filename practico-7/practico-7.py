import numpy as np;
import cv2;

def getImage():
    return cv2.imread('paisaje.jpg')

def saveNewImg(img):
    cv2.imwrite("imagen-rotada-escalada.jpg", img)

def rotate(img, angle, center=None, scale=1.0):
    (height, width) = (img.shape[:2])

    if center is None:
        center = (width/2, height/2)

    matrix = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(img, matrix, (width, height))

def traslate(img, x, y, scale):
    (height, width) = (img.shape[0], img.shape[1])
    matrix = np.float32([[scale*1, scale*0, x], [-scale*0, scale*1, y]])
    return cv2.warpAffine(img, matrix, (width, height))

def euclideanTransformation(img, angle, xTraslation, yTraslation, scale):
    rotated = rotate(img, angle)
    return traslate(rotated, xTraslation, yTraslation, scale)

def closeWindows():
    cv2.destroyAllWindows()

def init ():
    if key == ord('g'):
        saveNewImg(euclideanImg)
        closeWindows()
    else:
        closeWindows()

image = getImage()
euclideanImg = euclideanTransformation(image, -60, 25, 30, 0.5)
cv2.imshow('image', euclideanImg)
key = cv2.waitKey(0)
init()
