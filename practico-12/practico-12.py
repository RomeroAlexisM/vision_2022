import numpy as np;
import cv2;

MIN_MATCH_COUNT = 30

def getImage(imgName):
    imgReaded = cv2.imread(imgName)
    return cv2.resize(imgReaded,(800, 600), interpolation=cv2.INTER_CUBIC)

def closeWindows():
    cv2.destroyAllWindows()
    
def siftImage(firstImg, secondImg):
    global MIN_MATCH_COUNT
    dscr = cv2.SIFT_create()    # Inicializamos el detector y el descriptor
    kp1, des1 = dscr.detectAndCompute(firstImg, None)   # Encontramos los puntos clave y los descriptores con SIFT en la imagen 1
    kp2, des2 = dscr.detectAndCompute(secondImg, None)  # Encontramos los puntos clave y los descriptores con SIFT en la imagen 2
    matcher = cv2.BFMatcher(cv2.NORM_L2)
    matches = matcher.knnMatch(des1, des2, k=2)
    
    # Guardamos los buenos matches usando el test de razón de Lowe
    good = []

    for m, n in matches:
        if(m.distance < (0.60 * n.distance)):
            good.append(m)
        
    if(len(good) > MIN_MATCH_COUNT):
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        H, mask = cv2.findHomography(dst_pts,src_pts,cv2.RANSAC,5.0)    #Computamos la homografía con RANSAC
        matchesMask = mask.ravel().tolist()
        
    wimg2 = cv2.warpPerspective(secondImg, H, (800,600))    # Aplicamos la transformación perspectiva H a la imagen 2
  
    # Mezclamos ambas imágenes
    alpha = 0.5
    return np.array(wimg2 * alpha + firstImg * (1 - alpha), dtype=np.uint8), drawPointMatches(firstImg, kp1, secondImg, kp2, good, matchesMask)

def drawPointMatches(firstImg, kp1, secondImg, kp2, good, matchesMask):
    draw_params = dict(matchColor = None, # Dibujar puntos en común
                   matchesMask = matchesMask, # Dibujar lineas entre los puntos
                   singlePointColor = None,
                   flags = 2)

    return cv2.drawMatches(firstImg, kp1 , secondImg, kp2, good, None, **draw_params)


def init():
    firstImg = getImage("img1.jpeg")
    secondImg = getImage("img2.jpeg")
    blend, imgWithMatches = siftImage(firstImg, secondImg)
    cv2.imshow("Puntos en comun", imgWithMatches)
    cv2.imshow("Resultado", blend)
    
    while (1):
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            closeWindows()
            break
            
init()
