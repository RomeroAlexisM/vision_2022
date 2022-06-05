import numpy as np;
import cv2;

def getImage(imgName):
    return cv2.imread(imgName)

def saveNewImg(img):
    cv2.imwrite("imagen-rectificada.jpg", img)

def getRectifiedImg():
    WIDTH = selectedPoints[1][0] - selectedPoints[0][0]
    HEIGHT = selectedPoints[3][1] - selectedPoints[0][1]
    if(WIDTH > 0 and HEIGHT > 0):
        pst1 = np.float32([selectedPoints])
        pts2 = np.float32([[0, 0], [WIDTH, 0], [WIDTH, HEIGHT], [0, HEIGHT]])
        M = cv2.getPerspectiveTransform(pst1, pts2)
        return cv2.warpPerspective(firstImg, M, (WIDTH, HEIGHT))
    
def closeWindows():
    cv2.destroyAllWindows()
        
def drawDot(event, x, y, flags, param):
    global firstImgCopy

    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(firstImgCopy, (x, y), 2, (0, 255, 5), 4)
        appendNewPoint([x, y])

def appendNewPoint(point):
    global counter
    selectedPoints.append(point)
    counter += 1

def init():
    global firstImgCopy, firstImg
    cv2.namedWindow(winname= "Rectificando imágenes")
    cv2.setMouseCallback("Rectificando imágenes", drawDot)

    while counter != 4:
        cv2.imshow("Rectificando imágenes", firstImgCopy)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            closeWindows()
            break
        elif key == ord('r'):
            firstImgCopy = firstImg.copy()
            
    saveNewImg(getRectifiedImg())
    
            
    while(1):
        cv2.imshow("Imagen rectificada", getRectifiedImg())
        key = cv2.waitKey(1) & 0xFF
        if key ==  ord('q'):
            break
            
       
firstImg = getImage("cartas.jpg")
firstImgCopy = firstImg.copy()
selectedPoints = []
counter = 0
rows, cols, ch = firstImgCopy.shape

init()