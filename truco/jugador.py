class Jugador:
    def __init__(self,nombre,numero, System):
        self.nombre = nombre
        ## self.cantVictorias = cantVictorias //Para un futuro.
        self.numero = numero
        self.carta1 = None
        self.carta2 = None
        self.carta3 = None
        self.system = System
    end

    def designarCartas(self,cartas):
        self.carta1= cartas[0]
        self.carta2= cartas[1]
        self.carta3= cartas[2]
    end
    
    def designarNumero(self,numero):
        self.numero = numero
    end

    def elegirCarta(carta):
        if carta != None: 
            self.system.jugarCarta(carta)
            if carta == self.carta1:
                carta1 = None
            if carta == self.carta2:
                carta2 = None
            if carta == self.carta3:
                carta3 = None
        else: ##Error de Jugar inválida


