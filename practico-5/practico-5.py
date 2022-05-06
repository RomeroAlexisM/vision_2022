import cv2
import numpy as np

def getImage():
    return cv2.imread('paisaje.jpg')

def saveNewImg(img):
    cv2.imwrite("imagen-recortada.jpg", img)

def selectInImage(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, imgCopy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True: 
            imgCopy = getImage()
            cv2.rectangle(imgCopy, (ix,iy), (x,y), (0,0,0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        imgCopy = getImage()
        fx, fy = x, y
        cv2.rectangle(imgCopy,(ix,iy),(x,y),(0,0,0),2)

def cropAndSave(x, y):
    imageOut = imgCopy[iy:y,ix:x]
    saveNewImg(imageOut)
    closeWindows()

def closeWindows():
    cv2.destroyAllWindows()

def initWindows():
    cv2.namedWindow('Crop Image')
    cv2.setMouseCallback('Crop Image', selectInImage)

def init():
    initWindows()
    global imgOriginal, imgCopy
    while(1):
        cv2.imshow('Crop Image',imgCopy)
        k = cv2.waitKey(1)&0xFF
        if k == ord('r'):
            imgCopy = imgOriginal.copy()
        elif k == ord('g'):
            cropAndSave(fx, fy)
            break
        elif k == 27:
            closeWindows()
            break

drawing = False
ix , iy= -1, -1
fx , fy= -1, -1
imgOriginal = getImage()
imgCopy = imgOriginal.copy()
init()