import numpy as np    
import math
import matplotlib.pyplot as plt 
from PIL import Image  
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
