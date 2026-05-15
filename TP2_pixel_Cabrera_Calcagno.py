import os
import numpy as np    
import math
import matplotlib.pyplot as plt 
from PIL import Image  

#PIXEL ART:
def pixel_art (imagen: Image.Image, niveles: int, tam_bloque: int)-> Image.Image:
    
    """
    Convierte la imagen a un array Numpy. Recorre en bloques cuadrados y 
    remplaza cada bloque por el color de paleta mas ceercano a su promedio RGB.

    ARGUMENTOS 
    imagen: imagen de entrada 
    niveles: cantidad de niveles de canales, determina el
    tamaño de la paleta de colores
    tam_bloque: longitud en pixeles de los lados de cada bloque

    RETURN 
    La funcion retonra una nueva imagen con el efecto pixel art ya aplicado
    """

    array_imagen = np.array (imagen)
    alto= array_imagen.shape[0]
    ancho= array_imagen.shape[1]

    valores_posibles = [0]

    for i in range(niveles-1):
        x = 255 // (niveles - 1)
        proximo_valor = valores_posibles[-1] + x 
        valores_posibles.append(proximo_valor)

    for i in range (0,alto,tam_bloque):
        for j in range (0,ancho,tam_bloque):
            bloque = array_imagen [i:i+tam_bloque, j:j+tam_bloque]
            promedio = np.mean(bloque,axis=(0,1))
            mas_cercano= [min(valores_posibles, key=lambda x: abs(x-canal)) for canal in promedio]
            bloque [:]= mas_cercano

    imagen_modificada= Image.fromarray(array_imagen)

    return imagen_modificada

#PREGUNTA PARA USO DE PIXEL ART
 
def pixel(imagen:Image.Image )-> Image.Image :
    
    """
    Se pregunta al usuario por tamaño de bloque y cantidad de niveles,
    en caso de que no se le asigne valor. Sino, se valida que los
    valores ingresados sean positivos.
   
    ARGUMENTO
    imagen: Imagen de entrada a convertir en pixel art

    RETURN
    La funcion retorna la imagen con el efecto pixel art, segun parametros
    ingresados por el usuario.
    """

    entrada = input('Ingrese tamaño del bloque (default=10): ')
    if entrada == '' or entrada == ' ':
        tamaño = 10
    else:
        while not entrada.isdigit() or tamaño <= 0:
            entrada= input ('Reingrese el tamaño:')                         
        tamaño = int(entrada)

    
    n= (input("ingrese niveles"))
    if n == '' or n == " ":
        niveles = 4
    else:
        while not n.isdigit() or niveles <= 0:
            n= input ('Reingrese el tamaño: ')
        niveles = int(n)
    nueva_imagen= pixel_art(imagen,niveles,tamaño)

    return nueva_imagen
