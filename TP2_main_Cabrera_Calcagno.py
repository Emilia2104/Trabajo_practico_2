from TP2_ascii_Cabrera_Calcagno import *
from TP2_funciones_Cabrera_Calcagno import *
from TP2_pixel_Cabrera_Calcagno import *

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
