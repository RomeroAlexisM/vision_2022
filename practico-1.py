import random

def obtenerNumero():
    return random.randint(0,100) 

def mostrarMensajeExisto(numeroDeIntento: int):
    print('******************************')
    print('* ¡¡¡Adivinaste el número!!! *')
    print('* Cantidad de intetos: %d    *' % numeroDeIntento)
    print('******************************')

def mostrarMensajeFracaso():
    print('Vuelve a intentarlo...')
    
def mostrarMensajePerdiste():
    print('**********************')
    print('* ¡¡¡Mala Suertes!!! *')
    print('* ¡¡¡Haz perdido!!!  *')
    print('**********************')

def analizarNumero(intentos: int, numeroIngresado: int, numeroDeIntento: int, numeroHaAdivinar: int):
    if(intentos >= 0):
        if numeroHaAdivinar == numeroIngresado:
            mostrarMensajeExisto(numeroDeIntento)
            return True
        else:
            mostrarMensajeFracaso()
            return False
    else:
        mostrarMensajePerdiste()
        return None  

def adivinar(intentos: int):
    numeroHaAdivinar: int = obtenerNumero()
    numeroDeIntento: int = 1
    terminoElJuego: bool = False

    print('¡¡¡Adivina el número!!!')

    while (terminoElJuego == False):
        print('Cantidad de intentos: %d' % intentos)
        intentos -= 1
        numeroIngresado: int = int(input('Ingresa un número entre 0 y 100: '))
        terminoElJuego = analizarNumero(intentos, numeroIngresado, numeroDeIntento, numeroHaAdivinar)
        numeroDeIntento += 1
        
def iniciar():
    INTENTOS: int = 10
    adivinar(INTENTOS)

iniciar()