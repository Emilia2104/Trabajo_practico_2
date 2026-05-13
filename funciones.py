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
        while not entrada.isdigit():
            entrada= input ('Reingrese el tamaño:')
                            
        ancho = int(entrada)
        while ancho <= 0:
            entrada = input('Ancho de la imagen ASCII debe ser un numero positivo, reingrese: ')
            ancho = int(entrada)
            
    ruta_salida= input ("Ingrese nombre de la ruta para guardar el resultado: ") + "txt"
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
            flag = True
            resultado = pixel(imagen)
            resultado.show()
        elif entrada.lower() == "ascii":
            flag = True
            ascii(imagen)
        else:
            entrada = input ('Metodo invalido, ingrese pixel o ASCII')

main ()


