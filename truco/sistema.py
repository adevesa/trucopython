from NaipesEspanioles import baraja_truco, get_n_cards

from match import Match
from jugador import Jugador

class Sistema:
    Jugadores = []
    Flor = None
    ATreinta = None
    Maximo = 15 if not ATreinta else 30
    Baraja = None
    EsMano = None
    MatchEnJuego = None
    PuntajeEQ1 = 0
    PuntajeEQ2 = 0

    ## @func agregarJugador: agrega al sistema los jugadores que recibe desde el servidor y le asigna un equipo
    ## @param: jugadores_recibidos: lista de objetos Jugador

    def agregarJugador(self, jugadores_recibidos):
        equipo = 1
        for jugador in jugadores_recibidos:
            self.Jugadores.append((jugador,equipo))
            if equipo == 1: 
                equipo = 2 
            else: equipo = 1

    ## @func: barajar: crear una baraja de truco y la asigna al sistema
    ## @param: Nada

    def barajar(self):
        self.Baraja = baraja_truco()

    ## @func: definir_puntaje: define el puntaje (15/30)
    ## @param: True or false

     def definir_puntaje(self, YoN):
        self.ATreinta = YoN

    ## @func: definir_flor: habilita o no flor
    ## @param: True or false

    def definir_flor(self, YoN):
        self.Flor = YoN

    ## @func: repartir_cartas: le da 3 cartas a cada jugador
    ## @param: Baraja

    def repartir_cartas(self):
        for Jugador in Jugadores:
            Jugador.designarCartas(get_n_cards(self.baraja,3))

    ## @func: crear_match: crear un objeto match
    ## @param: void

    def crear_match(self):
        self.MatchEnJuego = Match(self.Jugadores, self.EsMano, self)

    ## @func: aumentar_puntaje: aumenta el puntaje de los equipos
    ## @param: Equipo, numerico, 1 o 2
    ##         puntaje, numerico, cuantos puntos aumenta el equipo

    def aumentar_puntaje(self, Equipo, puntaje):
        if Equipo = 1:
            self.PuntajeEQ1 = self.PuntajeEQ1 + puntaje
        elif Equipo = 2:
            self.PuntajeEQ2 = self.PuntajeEQ2 + puntaje
        detectar_ganador()
    
    ## @func: detectar_ganador: funcion auxiliar, para detectar si hubo algun equipo que alcanzó o superó el puntaje para ganar.
    ## @param: void

    def detectar_ganador(self):
        if self.PuntajeEQ1 >= self.Maximo:
            terminarTodo()
            ganador(Equipo1)
        if self.PuntajeEQ2 >= self.Maximo:
            terminarTodo()
            ganador(Equipo2)

    def orden_al_match(self, jugador, opcion):
        self.MatchEnJuego.tratarOpcion(jugador, opcion)
        

    



     
