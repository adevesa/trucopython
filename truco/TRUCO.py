## Truco.py

from NaipesEspanioles import (crear_baraja,
                              mezclar,
                              get_n_cards,
                              restringir_numero,
                              restringir_comodines,
                              empieza_jugador,
                              baraja_truco)

from envido import (tanto,
                    pelea_de_envidos,
                    envido_turno_propio)

from JerarquiaCartas import le_gana_a

from Textos import (mostrar_mano, ## param mano
                    mostrar_carta, ## param carta
                    mostrar_opciones, ## param cartas
                    settings_juego,
                    menu_principal,
                    seleccion) 

from IA import (lanzar_carta,
                cantar_envido,
                cantar_truco,
                cantar_retruco,
                cantar_vale_cuatro,
                querer_envido,
                querer_truco,
                querer_retruco,
                querer_vale_cuatro,
                irse_al_mazo)


                
class juegoTruco():
    Jugadores = (("JUGADOR 1", 0),
                 ("JUGADOR 2", 0))
    ENVIDO = 0
    TRUCO = 0
    P_MAX = 15
    
                
def main():
    opcion = menu_principal()
    if opcion == 1: JuegoTruco()
    if opcion == 2: Configuracion()
    
def JuegoTruco():
    Jugadores = 2 # leerConfig(jugadores)
    P_MAX = 15 # leerConfig(tanto)
    
    if Jugadores == 2: truco_de_a_dos(P_MAX)
    if Jugadores == 4: truco_de_a_cuatro(P_MAX)
    if Jugadores == 6: truco_de_a_seis(P_MAX)

    return "NADIE GANO"

def truco_de_a_dos(P_MAX):
    PUNTOS_JUGADOR_1 = 0
    PUNTOS_JUGADOR_2 = 0

    TURNO = empieza_jugador(2)

    while PUNTOS_JUGADOR_1 < P_MAX and PUNTOS_JUGADOR_2 < P_MAX:
        BARAJA = baraja_truco()

        ENVIDO = 0
        TRUCO = 1

        CARTAS_J1 = get_n_cards(BARAJA, 3)
        CARTAS_J2 = get_n_cards(BARAJA, 3)

        CARTAS_J1, CARTAS_J2, 
        ENVIDO, G_ENVIDO, TRUCO, GANADOR = primera_disputa(CARTAS_J1, CARTAS_J2, TURNO, PUNTOS_JUGADOR_1,PUNTOS_JUGADOR_2)

        # if PUNTOS_JUGADOR_1 + ENVIDO >= P_MAX: return "JUGADOR 1"
        # if PUNTOS_JUGADOR_2 + ENVIDO >= P_MAX: return "JUGADOR 2"

        # CARTAS_J1, CARTAS_J2, TRUCO, GANADOR = segunda_disputa(CARTAS_J1,CARTAS_J2,GANADOR)


        return

        '''
def primera_disputa(C1, C2, TURNO):
    mostrar_mano(C1)

    if TURNO == "JUGADOR 1":
        mostrar_opciones(C1)
        opcion = seleccion(["CARTA1",
                            "CARTA2",
                            "CARTA3",
                            "ENVIDO",
                            "REAL ENVIDO",
                            "FALTA ENVIDO",
                            "TRUCO",
                            "ME VOY AL MAZO"])
                            
    while opcion != 1 and opcion != 2 and opcion != 3:    
        
        if opcion == 4:
            ENVIDO == 1
            ##acepta envido por default
            ENVIDO == 2 
            
            G_ENVIDO = pelea_de_envidos(C1,C2,TURNO)
            opcion = seleccion(["CARTA1",
                                "CARTA2",
                                "CARTA3",
                                "TRUCO",
                                "ME VOY AL MAZO"])
            
        if opcion == 5 :
            ENVIDO == 1
            ##acepta el envido por default
            ENVIDO == 3
            
            G_ENVIDO = pelea_de_envidos(C1,C2,TURNO)
            opcion = seleccion(["CARTA1",
                                "CARTA2",
                                "CARTA3",
                                "TRUCO",
                                "ME VOY AL MAZO"])
            
 FALTA IMPLEMENTAR FALTA ENVIDO
        if opcion == 6
            ENVIDO == 1
            ##acepta el envido por default
            ENVIDO == 

        if opcion == 7:
            ##se acepta el truco por default.
            ##tambien se puede esperar un retruco
            
            TRUCO = 2
            opcion = seleccion(["CARTA1",
                                "CARTA2",
                                "CARTA3",
                                "ME VOY AL MAZO"])
        
    if opcion == 1 or opcion == 2 or opcion == 3:
           mi_carta == C1[opcion-1]
           del C1[opcion-1]
           respuesta = esperar_respuesta(C2)
                   if type(respuesta) == tuple
                    carta_rival = respuesta
                ## respuesta envido o lo que sea.
        
        '''
        


todas_las_opciones = ["CARTA1","CARTA2","CARTA3",
                      "ENVIDO","REAL ENVIDO","FALTA ENVIDO",
                      "TRUCO",
                      "ME VOY AL MAZO"]

def primera_disputa(CARTAS_J1, CARTAS_J2, TURNO, PJ1, PJ2):
    mostrar_mano(CARTAS_J1)
    
    if TURNO == "JUGADOR 1":
        mostrar_opciones(CARTAS_J1)
        opcion = seleccion(todas_las_opciones)
        
        if opcion == 5 or opcion == 6 or opcion == 7:
            ENVIDO, G_ENVIDO = envido_turno_propio(CARTAS_J1, CARTAS_J2, PJ1, PJ2, TURNO, opcion)
        print(ENVIDO)
        print(G_ENVIDO)
		
    return (0,0,0,0)
        
JuegoTruco()
