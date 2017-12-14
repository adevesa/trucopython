## ENVIDO.py

## ENVIDO
## SUMA LOS VALORES DE LAS CARTAS
## CASO INDIVIDUAL: TODOS LOS PALOS DISTINTOS
## SE CANTA EL MAYOR NUMERO
## 12 11 10 NO TIENEN VALOR
## CASO MULTIPLE: 2 O MAS PALOS REPETIDOS
## SE AGREGAN 20 Y SE SUMAN LOS PALOS DISTINTOS
## EJEMPLO:
## ESPADA 1 , ESPADA 2: = 23
## PALO 10, PALO 11: = 20

from IA import (querer_envido,
                querer_truco,
                querer_retruco,
                querer_vale_cuatro,
                irse_al_mazo)

from Textos import (quiero_no_quiero_envido,
                   	respuesta_envido,
                    el_envido_primero,
                    mostrar_envido)					

'''
@func: tanto
@param: cartas
@desc:  dado una mano de 3 cartas, devuelve su puntaje para el envido.
        Primero se fija si las 3 cartas son distintas, si lo son, devuelve su puntaje individual
        sino, devuelve su puntaje teniendo en cuenta que hay mas de un palo igual
'''
				
def tanto(cartas):
    if son_palos_distintos(cartas):
        puntillos = maximo_puntaje_individual(cartas)
    else:
        puntillos = maximo_puntaje_multiple(cartas)
    return puntillos
    end
'''
@func: son_palos_distintos
@param: cartas
@desc:  dado una mano de 3 cartas, devuelve True SI todas sus cartas son de distintos palos.
        En caso de que haya un par igual, devuelve False.
'''

def son_palos_distintos(cartas):
    if (cartas[0][0] == cartas[1][0] or
        cartas[1][0] == cartas[2][0] or
        cartas[2][0] == cartas[0][0]): return False
    else: return True

'''
@func: maximo_puntaje_individual
@param: cartas
@desc:  dado una mano de 3 cartas, devuelve su puntaje para el envido.
        Primero se fija si las 3 cartas son distintas, si lo son, devuelve su puntaje individual
        sino, devuelve su puntaje teniendo en cuenta que hay mas de un palo igual
'''

def maximo_puntaje_individual(cartas):
    maximo = 0
    for carta in cartas:
        if es_doce_once_o_diez(carta):
            if maximo == 0: maximo = 0
        elif carta[1] > maximo: maximo = carta[1]
    return maximo

'''
@func: maximo_puntaje_multiple
@param: cartas
@desc:  dado una mano de 3 cartas, devuelve su puntaje para el envido.
        Suma el puntaje de dos palos iguales.
        Si hay 3 palos iguales, elige las dos mejores.
       
'''

def maximo_puntaje_multiple(cartas):
    maximoOro = 20
    maximoBas = 20
    maximoCop = 20
    maximoEsp = 20

    if tres_palos_iguales(cartas):
       return los_dos_mejores(cartas) 
    else:
        for carta in cartas:
            if not es_doce_once_o_diez(carta):
                if carta[0] == "ORO": maximoOro += carta[1]
                if carta[0] == "BASTO": maximoBas += carta[1]
                if carta[0] == "COPA": maximoCop += carta[1]
                if carta[0] == "ESPADA": maximoEsp += carta[1]
    maximo = max(maximoOro,maximoBas,maximoCop,maximoEsp)

    return maximo

'''
@func: tres_palos_iguales
@param: cartas
@desc: Si los tres palos son iguales devuelve True, sino false.
'''

def tres_palos_iguales(cartas):
    if cartas[0][0] == cartas[1][0] and cartas[1][0] == cartas[2][0]: return True
    else: False

'''
@func: los_dos_mejores
@param: cartas
@desc: devuelve el puntaje de las mejores cartas de las tres iguales.
'''

def los_dos_mejores(cartas): 
    carta1 = 0 if es_doce_once_o_diez(cartas[0]) else cartas[0][1] ##TERNARY OPERATORS 
    carta2 = 0 if es_doce_once_o_diez(cartas[1]) else cartas[1][1] ##TERNARY OPERATORS
    carta3 = 0 if es_doce_once_o_diez(cartas[2]) else cartas[2][1] ##TERNARY OPERATORS
    
    lista = [carta1, carta2, carta3]
    lista.sort()
    return 20 + lista[2] + lista[1]

'''
@func: es_doce_once_o_diez
@param: carta
@desc: retorna True si es 10 11 o 12.
'''

def es_doce_once_o_diez(carta):
    if carta[1] == 12 or carta[1] == 11 or carta[1] == 10: return True
    else: return False

'''
    Respuestas y procesos... REVISAR.
'''

    
def pelea_de_envidos(C1,C2,TURNO):
    if tanto(C2) > tanto(C1):
        G_ENVIDO = "JUGADOR 2"
    elif tanto(C2) == tanto(C1):
        if TURNO == "JUGADOR 2": G_ENVIDO = "JUGADOR 2"
        else: G_ENVIDO = "JUGADOR 1"
    else: G_ENVIDO = "JUGADOR 1"    
    
    return G_ENVIDO

opciones_sin_envido = ["CARTA1","CARTA2","CARTA3",
                      "TRUCO",
                      "ME VOY AL MAZO"]
                      
resp_al_envido = ["ENVIDO","REAL ENVIDO","FALTA ENVIDO",
                  "ME VOY AL MAZO"]
                  
resp_al_envido_envido = ["REAL ENVIDO","FALTA ENVIDO",
                         "ME VOY AL MAZO"]
                         
falta_me_voy_mazo = ["FALTA ENVIDO",
                     "ME VOY AL MAZO"]
                     
me_voy_al_mazo = ["ME VOY AL MAZO"]    
    
    
def envido_turno_propio(CARTAS_J1, CARTAS_J2, PJ1, PJ2, TURNO, opcion):
    
    ## RECIBO ENVIDO
    if opcion == 5: 
        ENVIDO = 1 
        resp = querer_envido("NADA",CARTAS_J2)
        if resp: 
            ENVIDO = 2
            G_ENVIDO = pelea_de_envidos(CARTAS_J1, CARTAS_J2, TURNO)
        if not resp:
           G_ENVIDO = "JUGADOR 1"
        ## TRATAR OTRA RESP
        
    if opcion == 6:
        ENVIDO = 1
        resp = querer_envido("NADA", CARTAS_J2)
        if resp:
           ENVIDO = 3
           G_ENVIDO = pelea_de_envidos(CARTAS_J1, CARTAS_J2, TURNO)
           ## TRATAR OTRAS RESP
        if not resp:
           G_ENVIDO = "JUGADOR 1"
           
    if opcion == 7:
        ENVIDO = 1
        resp = querer_envido("NADA",CARTAS_J2)
        if resp: 
            ENVIDO = 15 - max(PJ1,PJ2)
            G_ENVIDO = pelea_de_envidos(CARTAS_J1, CARTAS_J2, TURNO)
        if not resp:
           G_ENVIDO = "JUGADOR 1"
        ## TRATAR OTRAS RESP
    
    return ENVIDO, G_ENVIDO
	
def responder_envido(CANTO, CARTAS_J1, CARTAS_J2,):
    if CANTO == "ENVIDO":
	   opcion = quiero_no_quiero_envido(CARTAS_J1)
       if opcion == 1:
	      mostrar_envido(CARTAS_J2)
		  if tanto(CARTAS_J1) > tanto(CARTAS_J2)
		  opcion_2 = 




''' TESTS
from NaipesEspanioles import (crear_baraja,
                              mezclar,
                              get_n_cards,
                              restringir_numero,
                              restringir_comodines)
                            
b = crear_baraja()
b = restringir_comodines(b)
b = restringir_numero(b,8)
b = restringir_numero(b,9)
m = mezclar(b)


i = 0
while i < 10:
    n = get_n_cards(m,3)
    k = get_n_cards(m,3)
    print(n)
    print("---")
    print(tanto(n))
    print("---")
    print(k)
    print("---")
    print(tanto(k))
    print(pelea_de_envidos(n,k,"JUGADOR 1"))
    i = i + 1

    '''
