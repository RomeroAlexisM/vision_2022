import cv2 as cv

def obtenerImagen():
    return cv.imread('imagen.png', 0)

def aplicarUmbral(imagen):
    imagen[imagen>210] = 255
    imagen[imagen!=255] = 0
    return imagen

def guardarImagenModificada(imagen):
    cv.imwrite("imagen-modificada.png", imagen)

def iniciar():
    print("Obteniendo Imagen")
    imagen = obtenerImagen()
    print('Imagen obtenida')
    print('Aplicando umbral...')
    imagenModificada = aplicarUmbral(imagen)
    guardarImagenModificada(imagenModificada)
    print('Imagen modificada guardada')

iniciar()
