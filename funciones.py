import numpy as np    
import math
import matplotlib.pyplot as plt 
from PIL import Image  
#PIXEL:
def pixel(imagen, tamaño, niveles):
    array_imagen = np.array (imagen)
    alto= array_imagen.shape[0]
    ancho= array_imagen.shape[1]
    #tenemos que hacer una variable con los valores posibles por nivel, que empieza en 0 y dividimos 255 (que es el maximo del canal) por la cantidad de niveles - 1 y lo sumamos al ultimo numero

    # Recorremos la imagen bloque por bloque saltando de a tamaño de bloque que nos da el input 
    # En cada iteración, i y j son la esquina superior izquierda del bloque actual
    # Hacemos una variable bloque , calculamos su color promedio y lo reemplazamos por el color más cercano de la paleta




#ASCII:
def trabajo_ascii(imagen, ancho):
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

def guardar_ascii_art(ascii_art: str, ruta_salida: str):
    with open(ruta_salida, 'w') as f:
        f.write(ascii_art)


def ascii (imagen,ruta_salida):
    entrada = input('Ingrese ancho de imagen (default=100): ')
    ancho = 100 if entrada == '' else int(entrada)
    resultado= trabajo_ascii (imagen,ancho)
    guardar_ascii_art(resultado,ruta_salida)




