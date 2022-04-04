
import cv2 as cv

def guardarImagenModificada(imagen):
    print('Guardando Imagen')
    cv.imwrite("imagen-guardada.jpeg", imagen)

def cerrarVentana():
    cv.destroyAllWindows( )

def leerImagen():
    return cv.imread('imagen.jpeg')

def mostrarImagen(img):
    cv.imshow('imagen', img)
    key = cv.waitKey(0)
    definirAccion(key, img)

def definirAccion(key, img):
    if(key == ord('s')):
        guardarImagenModificada(img)
    else:
        cerrarVentana()

def iniciar():
    img = leerImagen()
    mostrarImagen(img)

iniciar()