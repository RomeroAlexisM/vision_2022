import numpy as np;
import cv2;
import  math

def getImage(imgName):
    imgReaded = cv2.imread(imgName)
    return cv2.resize(imgReaded,(800, 600), interpolation=cv2.INTER_CUBIC)

def getRatioFromReference(FIRST_POINT, SECOND_POINT, THIRD_POINT, FOURTH_POINT):
    global ratio, euclideanDistanceReference 
    referenceWidthPx = SECOND_POINT[0] - FIRST_POINT[0]
    
    euclideanDistanceReference = math.sqrt(math.pow(referenceWidthPx, 2) + 
                            math.pow(FOURTH_POINT[1] - THIRD_POINT[1], 2))
    
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
   
    #Puntos de referencia
    FIRST_POINT = [155, 142]
    SECOND_POINT = [401, 139]
    THIRD_POINT = [396, 460]
    FOURTH_POINT = [160, 438]  

    ratio = getRatioFromReference(FIRST_POINT, SECOND_POINT, THIRD_POINT, FOURTH_POINT)      
    counter = 0
    selectedPoints = []
    getMeasurement()
    

#Referencia alto y ancho de la ventana en metros
REFERENCE_WIDTH_METERS = 1.24
REFERENCE_HEIGHT_METERS = 1.52

euclideanDistanceReference = 0
ratio = 0
firstImg = getImage("img1.jpeg")
firstImgCopy = firstImg.copy()
counter = 0

init()

