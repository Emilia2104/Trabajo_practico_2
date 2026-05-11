import os
import numpy as np    
import math
import matplotlib.pyplot as plt 
from PIL import Image  

#PIXEL:
def pixel_art (imagen, niveles, tam_bloque):
    array_imagen = np.array (imagen)
    alto= array_imagen.shape[0]
    ancho= array_imagen.shape[1]

    valores_posibles = [0]
    for i in range(niveles-1):
        x = 255 // (niveles - 1)
        proximo_valor= valores_posibles[-1] + x 
        valores_posibles.append(proximo_valor)

    for i in range (0,alto,tam_bloque):
        for j in range (0,ancho,tam_bloque):
            bloque = array_imagen [i:i+tam_bloque, j:j+tam_bloque]
            promedio = np.mean(bloque,axis=(0,1)).astype(np.uint8)
            mas_cercano= [min(valores_posibles, key=lambda x: abs(x-canal)) for canal in promedio]
            bloque [:]= mas_cercano
    imagen_modificada= Image.fromarray(array_imagen)
    return imagen_modificada

#pregunta pixel_art 
def pixel(imagen):
    
    entrada = input('Ingrese tamaño del bloque (default=10): ')
    if entrada == '' or entrada == ' ':
        tamaño = 10
    else:
        while not entrada.isdigit():
            entrada= input ('Reingrese el tamaño:')
                            
        tamaño = int(entrada)
        while tamaño <= 0:
            entrada = input('Bloque invalido, reingrese: ')
            tamaño = int(entrada)
    
    n= (input("ingrese niveles"))
    if n == '' or n == " ":
        niveles = 4
    else:
        while not n.isdigit():
            n= input ('Reingrese el tamaño: ')
        niveles = int(n)
        while niveles <= 0:
            n= input('Nivel invalido (0 o negativo),reingrese cantidad de niveles: ')
            niveles = int(n)

    nueva_imagen= pixel_art(imagen,niveles,tamaño)

    return nueva_imagen

    
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


def ascii (imagen):
    entrada = input('Ingrese ancho de imagen (default=100): ')

    if entrada == '' or entrada == ' ':
                ancho = 100
    else:
        while not entrada.isdigit():
            entrada= input ('Reingrese el tamaño:')
                            
        ancho = int(entrada)
        while ancho <= 0:
            entrada = input('Ancho de la imagen ASCII debe ser un numero positivo, reingrese: ')
            ancho = int(entrada)
            
    ruta_salida= input ("Seleccione la ruta para guardar el resultado: ")
    resultado= trabajo_ascii (imagen,ancho)
    guardar_ascii_art(resultado,ruta_salida)



#FUNCION SOLICUT DE RUTA Y MAIN
def solicitud()-> str:
    """
    Solicita al usuario la ruta donde esta la imagen, si no es valida solicita su reingreso

    Returns:
        str: Retorna ruta valida de la imagen
    """
    ruta= input('Ingrese ruta donde esta la imagen a procesar:')
    while not os.path.exists(ruta):
        ruta= input('No se encontro la imagen. Por favor, verifique la ruta e intente nuevamente: ')
    return ruta


def main(): 
    ruta = solicitud()
    entrada = input ('Seleccione metodo (pixel/ascii):')
    imagen= Image.open(ruta)
    flag= False
    while not flag:
        if entrada.lower() == "pixel":
            pixel(imagen)
        elif entrada.lower() == "ascii":
            ascii(imagen)
        else:
            entrada = input ('Metodo invalido, ingrese pixel o ASCII')
            flag = True

    main()
        
        
        

