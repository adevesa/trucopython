## Textos.py

protocolo = { "CARTA1":        1,
              "CARTA2":        2,
              "CARTA3":        3,
			  "TRUCO":         4,
			  "RETRUCO":       4,
			  "VALE CUATRO":   4,
              "ENVIDO":        5,
              "REAL ENVIDO":   6,
			  "FALTA ENVIDO":  7,
              "ME VOY AL MAZO":9,
			  "QUIERO":        1,
			  "NO QUIERO":     2,
	}
	
from envido import tanto 	

def mostrar_mano(mano):
    n = 1
    print('Tus cartas son:')
    for carta in mano:
        print ('({0})'.format(n) + mostrar_carta(carta))
        n = n + 1
          
def mostrar_carta(carta):
    if carta[0] != "COMODIN":
        return 'Palo: {0}\t Numero: {1}'.format(carta[0],carta[1])
    else:
        return('COMODIN')
    return

def mostrar_opciones(cartas):
    print("(4) TRUCO")
    if len(cartas) == 3:
        print("(5) ENVIDO\t\t" + "TANTO:({0})".format(tanto(cartas)))
        print("(6) REAL ENVIDO\t\t" + "TANTO:({0})".format(tanto(cartas)))
        print("(7) FALTA ENVIDO\t" + "TANTO:({0})".format(tanto(cartas)))
    print("(9) ME VOY AL MAZO")
    return
     
def settings_juego():
    print("CONFIGURACION: ")
    print("(1) JUGADORES: ")
    print("(2) FLOR: ")
    return
     
def menu_principal():
    print("TRUCO ARGENTINO: ")
    print("(1) JUEGO NUEVO")
    print("(2) CONFIGURACION")
    print("(3) SALIR")
    return("NADA")

def seleccion(permitidos2):
    permitidos = codificar_permitidos(permitidos2)
    opcion = input("SELECCIONE UNA OPCIÓN: ")
    try:
        if int(opcion) in permitidos: return int(opcion)
        else: 
            print("OPCIÓN INVALIDA")
            return seleccion(permitidos2)        
    except ValueError:
        print("OPCIÓN INVALIDA")
        return seleccion(permitidos2)

def codificar_permitidos(permitidos):
    permitidos_num = []
    for permitido in permitidos:
        permitidos_num.append(protocolo[permitido])
    return permitidos_num
	
def quiero_no_quiero():
    print("(1) QUIERO")
	print("(2) NO QUIERO")
	return seleccion(["QUIERO", "NO QUIERO"])

def el_envido_primero():
    print("EL ENVIDO ESTA PRIMERO ")
	opcion = quiero_no_quiero()
	if opcion == 1
	   