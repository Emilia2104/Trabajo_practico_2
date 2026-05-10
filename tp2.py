import numpy as np    
import math
import matplotlib.pyplot as plt 
from PIL import Image  

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


imagen = "foto.jpg"
# Cargar la imagen y convertirla a un array de NumPy


array_imagen = np.array(Image.open(imagen))


print("Dimensiones de la imagen:", array_imagen.shape)  # (alto, ancho, canales)
print("Tipo de datos:", array_imagen.dtype)

#DIVISON DE BLOQUES

alto, ancho = array_imagen.shape[:2] #valores de alto y ancho de la imagen en tupla

bloque_vertical = alto // 3
bloque_horizontal = ancho // 3
total_bloques = bloque_vertical * bloque_horizontal

for filas in range (0,alto,3):
    for columna in range (0,ancho,3):
        bloque1 = array_imagen[filas: filas+3, 0: 3] # bloque de 3x3
        bloque2 = array_imagen[columna: columna+3,0:3] # bloque de 3x3
        final = [bloque1, bloque2] # lista con los bloques
        print(final)





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



