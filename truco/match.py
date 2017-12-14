import random
from JerarquiaCartas import le_gana_a

class Match:
    g_env = None
    g_truco = None
    esMano = None
    le_toca_a = None
    system = None
    
    def __init__(self, Jugadores, esMano, System):
        self.Jugadores = Jugadores
        self.pEnvido = 0
        self.pTruco = 0
        self.sequence = []
        self.esMano = esMano if esMano != None else random.choice(Jugadores)
        self.le_toca_a = esMano
        self.system = System
            ## Si tiene un orden definido, respeta el orden, sino elige uno aleatorio.
    
    def _2_ganador_de(carta1,carta2):



    


        

        