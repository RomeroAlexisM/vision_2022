import numpy as np;
import cv2;
import  math

def getImage(imgName):
    imgReaded = cv2.imread(imgName)
    return cv2.resize(imgReaded,(800, 600), interpolation=cv2.INTER_CUBIC)

def getRatioFromReference():
    global ratio, referenceWidthPx, euclideanDistanceReference
    referenceWidthPx = selectedPoints[1][0] - selectedPoints[0][0]
    
    euclideanDistanceReference = math.sqrt(math.pow(referenceWidthPx, 2) + 
                            math.pow(selectedPoints[1][1] - selectedPoints[0][1], 2))
    
    return referenceWidthPx / euclideanDistanceReference

def getMeasurement():
    global counter, firstImg, firstImgCopy, ratio, counter, selectedPoints, euclideanDistanceReference
    cv2.namedWindow(winname= "Calculo de distancia entre dos puntos")
    cv2.setMouseCallback("Calculo de distancia entre dos puntos", drawDot)

    while(1):
        while counter < 2:
            cv2.imshow("Calculo de distancia entre dos puntos", firstImgCopy)
            key = cv2.waitKey(1) & 0xFF
            if key ==  ord('q'):
                break
            elif key == ord('r'):
                firstImgCopy = firstImg.copy()
                counter = 0
                
        cv2.imshow("Calculo de distancia entre dos puntos", firstImgCopy)
        #En caso de que se agregue otros puntos, estos son borrados
        if counter > 2:
            counter = 2
            del selectedPoints[2:len(selectedPoints) - 1]

        euclideanDistance = math.sqrt(math.pow(selectedPoints[1][0] - selectedPoints[0][0], 2) + 
                                math.pow(selectedPoints[1][1] - selectedPoints[0][1],2))
        
        finalDistance = (euclideanDistance * REFERENCE_WIDTH_METERS) / euclideanDistanceReference
        if finalDistance > 0: 
            writeMeasurement(round(finalDistance * ratio, 4))
        
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
        if key == ord('r'):
            firstImgCopy = firstImg.copy()
            counter = 0
            selectedPoints.clear()

def writeMeasurement(distance):
    xPosition = ((selectedPoints[1][0] - selectedPoints[0][0]) / 2) + selectedPoints[0][0]
    yPosition = ((selectedPoints[1][1] - selectedPoints[0][1]) / 2) + selectedPoints[0][1]
    measurement = str(distance) + " Mts"
    newImg = firstImgCopy.copy()
    cv2.putText(newImg, measurement, (int(xPosition), int(yPosition)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 1, cv2.LINE_AA)
    cv2.imshow("Calculo de distancia entre dos puntos", newImg)

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
    global firstImgCopy, firstImg, counter, selectedPoints, ratio
    cv2.namedWindow(winname= "Tomar referencias de la imagen")
    cv2.setMouseCallback("Tomar referencias de la imagen", drawDot)

    while counter != 4:
        cv2.imshow("Tomar referencias de la imagen", firstImgCopy)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            closeWindows()
            break
        elif key == ord('r'):
            firstImgCopy = firstImg.copy()
            
    ratio = getRatioFromReference()      
    counter = 0
    firstImgCopy = firstImg.copy()
    selectedPoints = []
    getMeasurement()
    

#alto y ancho de la ventana en metros
REFERENCE_WIDTH_METERS = 1.24
REFERENCE_HEIGHT_METERS = 1.52

euclideanDistanceReference = 0
referenceWidthPx = 0
referenceHeightPx = 0
ratio = 0
firstImg = getImage("img1.jpeg")
firstImgCopy = firstImg.copy()
counter = 0
rows, cols, ch = firstImgCopy.shape
selectedPoints = []

init()

