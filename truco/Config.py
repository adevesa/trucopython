## Config.

import os.path
import string
import json

path = "C:/Users/DEVESA/Documents/GitHub/trucopython/truco/"

'''
@func:  leer_config
@param: EMPTY
@desc:  Lee el path de formato JSON,
        Cierra el archivo,
        Identifica los parametros
            -> JUGADORES, PUNTAJE Y FLOR
        Los guarda y los exporta al programa.

'''

def leer_config():
    file = open(path + "config.json", "r")
    archivo = file.read()
    file.close()
    
    configuracion = json.loads(archivo)
    JUGADORES = configuracion["JUGADORES"]
    PUNTAJE = configuracion["PUNTAJE"]
    FLOR = configuracion["FLOR"]
    return(JUGADORES,PUNTAJE,FLOR)
    end
    
'''
Testing:
    Modificar el archivo config.json y ver los resultados con:
    print(leer_config());
'''
