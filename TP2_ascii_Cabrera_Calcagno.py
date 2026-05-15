import numpy as np    
import math
import matplotlib.pyplot as plt 
from PIL import Image 
    
#ASCII:
def trabajo_ascii(imagen: Image.Image , ancho: int)-> str:

    """
    Convierte la imagen a un array Numpy con escala de grises, se normalizan al rango 
    0-255 en base al minimo y maximo de la imagen, se redimensiona y mapea la imagen 
    asignandole el caracter correspondiente segun el valor de intensidad. 

    ARGUMENTOS
    imagen: Imagen de entrada a convertir en ascii art 
    ancho: tamano que ingresa el usuario para redimensiona la imagen

    RETURN
    La funcion retorna un string con el efecto ASCII de la imagen ya aplicado
    """
    paleta = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    
    # convertir a grises
    imagen_gris = imagen.convert("L")
    array_gris = np.array(imagen_gris)
    
    # normalizar
    minimo = np.min(array_gris)
    maximo = np.max(array_gris)
    normalizado = (array_gris - minimo) / (maximo - minimo) * 255
    
    # redimensionar
    alto = array_gris.shape[0]
    nuevo_alto = int(ancho * (alto / ancho) * 0.45)
    imagen_normalizada = Image.fromarray(normalizado.astype(np.uint8))
    imagen_redim = imagen_normalizada.resize((ancho, nuevo_alto))
    array_redim = np.array(imagen_redim)

    # mapear pixeles a caracteres
    resultado = ''
    for x in array_redim:
        for y in x:
            i = round((1 - y / 255) * (len(paleta) - 1))
            resultado += paleta[i]
        resultado += "\n"
    
    return resultado

def guardar_ascii_art(ascii_art: str, ruta_salida: str) -> None:

    """
    Guarda un el str de ASCII art en un archivo texto

    ARGUMENTOS:
    ascii_art: string con contenido del ascii art a guardar
    ruta_salida: string con la ruta donde se quiere guardar el contenido de ascii_art
    
    """
    with open(ruta_salida, 'w') as f:
        f.write(ascii_art)


def ascii (imagen:Image.Image)-> None:
    """
    Solicita al usuario el ancho deseado y ruta de salida, corrobora que los inputs sean validos, en caso de que lo sean
    genera ascii art y lo guarda en un archivo

    ARGUMENTO:
    imagen: imagen a convertir en ascii
    """
    entrada = input('Ingrese ancho de imagen (default=100): ')

    if entrada == '' or entrada == ' ':
                ancho = 100
    else:
        while not entrada.isdigit() or ancho <= 0:
            entrada= input ('Reingrese el tamaño:')
                            
        ancho = int(entrada)

    ruta_salida= input ("Ingrese nombre de la ruta para guardar el resultado: ") + "txt"
    resultado= trabajo_ascii (imagen,ancho)
    guardar_ascii_art(resultado,ruta_salida)




