## Naipes Espanioles funciones.

from itertools import product, permutations
import random

''' @@Name:     crear_baraja
    @@Parm:        none
    @@Desc:        Crea los 50 naipes españoles, 12 de cada palo y los 2 comodines.
                Los Naipes estan constituido en una tupla (PALO, NUMERO)
                La baraja es una coleccion de Naipes.
                [("COPA",5),("BASTO",8)...]

'''
def crear_baraja():
    palo = ["BASTO", "ORO", "ESPADA", "COPA"]
    numero = range(1,13)
    comodines =[("COMODIN",1), ("COMIDIN",2)]
    baraja = (list(product(palo,numero)))
    baraja = baraja + comodines
    return baraja

''' @@Name:     mezclar
    @@Parm:     baraja
    @@Desc:     Devuelve una nueva baraja con el orden de las cartas cambiadas aleatoriamente
'''

def mezclar(baraja):
    i = 0
    cantCartas = len(baraja)
    ubicacionesRandom = []
    while i < cantCartas:
        nRandom = random.randint(0, cantCartas - 1)
        if nRandom not in ubicacionesRandom:
            ubicacionesRandom = ubicacionesRandom + [nRandom]
            i = i + 1
    barajaNew = []
    for ubic in ubicacionesRandom:
        barajaNew.append(baraja[ubic])
    return barajaNew
    
''' @@Name:     get_n_cards
    @@Parm:     baraja, N (numero de cartas)
    @@Desc:     Dado una baraja, devuelve la N cantidad de cartas y destruye esas cartas de la baraja.

'''
    
def get_n_cards(baraja,N):
    i=0
    Cartas = []
    if len(baraja) < N:
        cartasFaltantes = N - len(baraja)
        while i < len(baraja):
            Cartas.append(baraja[0])
            del baraja[0]
            i = i + 1
        baraja = mezclar(crear_baraja())
        print('No hay mas cartas disponibles, barajando....')
        return Cartas + get_n_cards(baraja, cartasFaltantes)
    else:
        while i < N:
            Cartas.append(baraja[0])
            del baraja[0]
            i = i + 1
    return Cartas
	
''' @@Name:     restringir_numero
    @@Parm:     baraja, numero
    @@Desc:     Dado una baraja, devuelve una baraja sin cartas con ese numero. No aplica para comodines.

'''
    
def restringir_numero(baraja, numero):
    palo = ["BASTO", "ORO", "ESPADA", "COPA"]
    restringidos = (list(product(palo,[numero])))
    for rest in restringidos:
        if(rest in baraja):
            del baraja[baraja.index(rest)]          
    return baraja
	
''' @@Name:     restrigir_palo
    @@Parm:     baraja, palo
    @@Desc:     Dado una baraja, devuelve una baraja sin el palo mencionado. No funciona con comodines.

'''
    
def restringir_palo(baraja, palo):
    numero = range(1,13)
    restringidos = (list(product([palo],numero)))
    for rest in restringidos:
        if(rest in baraja):
            del baraja[baraja.index(rest)]          
    return baraja
	
''' @@Name:     restringir_comodines
    @@Parm:     baraja
    @@Desc:     Dado una baraja, devuelve una baraja sin comodines.

'''

def restringir_comodines(baraja):
    comodines =[("COMODIN",1), ("COMIDIN",2)]
    for comodin in comodines:
        if(comodin in baraja):
            del baraja[baraja.index(comodin)]          
    return baraja
	
''' @@Name:     empieza_jugador
    @@Parm:     Jugadores
    @@Desc:     Dado una cantidad de jugadores, devuelve un string con "JUGADOR N" 
				indicando quien empieza, siendo N un numero entre 1 y 'Jugadores'.
				

'''
    
def empieza_jugador(Jugadores):
    turno = random.randint(1,Jugadores)
    return "JUGADOR " + str(turno)

''' @@Name:     baraja_truco
    @@Parm:     
    @@Desc:     Devuelve una baraja especializada para truco.
                

'''

def baraja_truco():
    baraja = crear_baraja()
    baraja = mezclar(baraja)
    baraja = restringir_numero(baraja,8)
    baraja = restringir_numero(baraja,9)
    baraja = restringir_comodines(baraja)

    return baraja

