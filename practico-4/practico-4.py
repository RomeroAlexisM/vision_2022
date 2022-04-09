import cv2 as cv

def obtenerfps(cap):
    fps = cap.get(cv.CAP_PROP_FPS)
    milisegundos = int(round((1/fps)*1000, 0))
    return milisegundos

def configurarVideoDeSalida(cap, width, height):
    fourcc = cv.VideoWriter_fourcc('X', 'V', 'I', 'D')
    out = cv.VideoWriter('output.avi', fourcc, obtenerfps(cap), (width, height))
    return out

def capturarVideo():
    return cv.VideoCapture('video.mp4')

def mostrarVideo(cap, out):
    while(cap.isOpened()):
        ret, frame=cap.read()
        if ret is True:
            out.write(frame)
            cv.imshow('frame',frame)
            if cv.waitKey(obtenerfps(cap)) & 0xFF == ord('q'):
                break
        else:
            break
    cerrarVentana(cap, out)

def cerrarVentana(cap, out):
    cap.release()
    out.release()
    cv.destroyAllWindows()

def iniciar():
    cap = capturarVideo()
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    out = configurarVideoDeSalida(cap, width, height)
    mostrarVideo(cap, out)

iniciar()
