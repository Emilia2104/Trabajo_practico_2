
import numpy as np    
import math
import matplotlib.pyplot as plt 
from PIL import Image  

#PIXEL:
def pixel_divison_en_bloques (imagen, niveles, tam_bloque):
    array_imagen = np.array (imagen)
    alto= array_imagen.shape[0]
    ancho= array_imagen.shape[1]

    alto_bloque = alto // tam_bloque
    ancho_bloque = ancho // tam_bloque

    total_bloques = alto_bloque * ancho_bloque

    bloques = []
    for i in range (0,alto,tam_bloque):
        for j in range (0,ancho,tam_bloque):
            bloque = array_imagen [i:i+tam_bloque, j:j+tam_bloque]
            bloques.append (bloque)
    return bloques

def valores_posibles (niveles):
    valores_posibles = []
    for i in range(niveles):
        x = i * 255 // (niveles - 1)
        valores_posibles.append(x)
    return valores_posibles

def bloque_promedio (bloque, niveles, tam_bloque):
    promedio = np.mean(bloque, axis=(0,1)).astype(np.uint8)
    return promedio

def color_mas_cercano (promedio, valores_posibles):
   


        



    





    #tenemos que hacer una variable con los valores posibles por nivel, que empieza en 0 y dividimos 255 (que es el maximo del canal) por la cantidad de niveles - 1 y lo sumamos al ultimo numero LISTO!!!!

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


def solicitud()-> str:
    """
    Solicita al usuario la ruta donde esta la imagen, si no es valida solicita su reingreso

    Returns:
        str: Retorna ruta valida de la imagen
    """
    ruta= input('Ingrese ruta donde esta la imagen a procesar:')
    while not os.path.exists(ruta):
        ruta= input('Ruta no valida, reingrese ruta')
    return ruta


def main(): 
    ruta = solicitud()
    entrada = input ('Seleccione metodo (pixel/ascii):')
    



