## Config.

import os.path
import string
path = "C:\\Users\\DEVESA\\AppData\\Local\\Programs\\Python\\Python36-32\\truco\\"

def leer_config():
    file = open(path + "config.txt", "r")
    cont = file.read()
    JUGADORES = cont.get_value("JUGADORES=")
    print(cont)
    print(JUGADORES)
    file.close()
	
def obtener_de(string, key):
    

	
leer_config()