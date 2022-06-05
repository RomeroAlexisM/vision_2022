import numpy as np;
import cv2;

def getImage(imgName):
    return cv2.imread(imgName)

def saveNewImg(img):
    cv2.imwrite("imagen-trasnformada.jpg", img)

def getAffineTransformImg():
    rows, cols, ch = firstImgCopy.shape
    pts1 = np.float32([selectedPoints])
    pts2 = np.float32([imagePoints])
    M = cv2.getAffineTransform(pts2, pts1)
    dst = cv2.warpAffine(secondImg, M, (cols, rows))
    grayDst = cv2.cvtColor(np.ascontiguousarray(dst), cv2.COLOR_RGB2GRAY)
    (_, mask) = cv2.threshold(grayDst, 0, 255, cv2.THRESH_BINARY) 
    maskInv = cv2.bitwise_not(mask) 
    maskedImage = cv2.bitwise_and(firstImg, firstImg, mask=maskInv) 
    finalImg = cv2.add(maskedImage, dst)
    return finalImg

def closeWindows():
    cv2.destroyAllWindows()
        
def drawDot(event, x, y, flags, param):
    global firstImgCopy

    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(firstImgCopy, (x, y), 2, (0, 0, 255), 4)
        appendNewPoint([x, y])

def appendNewPoint(point):
    global counter
    selectedPoints.append(point)
    counter += 1

def init():
    global firstImgCopy, firstImg
    cv2.namedWindow(winname= "Transformación afín - Incrustando imágenes")
    cv2.setMouseCallback("Transformación afín - Incrustando imágenes", drawDot)

    while counter != 3:
        cv2.imshow("Transformación afín - Incrustando imágenes", firstImgCopy)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            closeWindows()
            break
        elif key == ord('r'):
            firstImgCopy = firstImg.copy()
            
    saveNewImg(getAffineTransformImg())
       
firstImg = getImage("paisaje.jpg")
secondImg = getImage("catarata.jpg")
firstImgCopy = firstImg.copy()
selectedPoints = []
counter = 0
rows, cols, ch = firstImgCopy.shape
imagePoints = [[0, 0], [0, cols], [rows, cols]]

init()