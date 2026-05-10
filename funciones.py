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


