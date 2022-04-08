
import cv2 as cv
def capturarVideo():
    return cv.VideoCapture('video.mp4')

def obtenerfps(cap):
    fps = cap.get(cv.CAP_PROP_FPS)
    milisegundos = int(round((1/fps)*1000, 0))
    return milisegundos

def cerrarPrograma():
    print("No se puede abrir la camara")
    exit()

def mostrarVideo(cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv.imshow('frame', frame)
        if((cv.waitKey(obtenerfps(cap)) & 0xFF) == ord('q')) :
            break

def iniciar():
    cap = capturarVideo()

    if not cap.isOpened():
        cerrarPrograma()
        
    mostrarVideo(cap)
    cap.release()
    cv.destroyAllWindows()

iniciar()
