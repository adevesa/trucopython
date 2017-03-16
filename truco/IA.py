## IA.py
import random
'''
lanzar_carta
cantar_envido
cantar_truco
cantar_retruco
cantar_vale_cuatro
querer_envido
querer_truco
querer_retruco
querer_vale_cuatro
irse_al_mazo
esperar_respuesta
'''



def lanzar_carta(registro, mano):
    ## PROVISORIO - MEJORAR IA DEL OPENENTE
    m = len(cartas) - 1
    n = random.randint(0,m)
    carta = cartas[n]
    del cartas[n]
    return carta
    ## PROVISORIO - MEJORAR IA DEL OPONENTE
    
def cantar_envido(registro, mano):
    ## PROVISORIO - MEJORAR IA ENVIDO DEL OPONENTE
    n = random.randint(0,1)
    if n == 0: return False
    else: return True
    ## PROVISORIO - MEJORAR IA ENVIDO DEL OPONENTE
    
def cantar_truco(registro, mano):
    ## PROVISORIO - MEJORAR IA TRUCO DEL OPONENTE
    n = random.randint(0,1)
    if n == 0: return False
    else: return True
    ## PROVISORIO - MEJORAR IA TRUCO DEL OPONENTE
    
def cantar_retruco(registro, mano):
    ## PROVISORIO - MEJORAR IA RETRUCO DEL OPONENTE
    n = random.randint(0,1)
    if n == 0: return False
    else: return True
    ## PROVISORIO - MEJORAR IA RETRUCO DEL OPONENTE
    
def cantar_vale_cuatro(registro, mano):
    ## PROVISORIO - MEJORAR IA VALE CUATRO DEL OPONENTE
    n = random.randint(0,1)
    if n == 0: return False
    else: return True
    ## PROVISORIO - MEJORAR IA VALE CUATRO DEL OPONENTE
    
def querer_envido(registro, mano):
    ## PROVISORIO - MEJORAR IA QUERER ENVIDO DEL OPONENTE
    n = random.randint(0,1)
    if n == 0: return False
    else: return True
    ## PROVISORIO - MEJORAR IA QUERER ENVIDO DEL OPONENTE
    
def querer_truco(registro, mano):
    ## PROVISORIO - MEJORAR IA QUERER TRUCO DEL OPONENTE
    n = random.randint(0,1)
    if n == 0: return False
    else: return True
    ## PROVISORIO - MEJORAR IA QUERER TRUCO DEL OPONENTE
    
def querer_retruco(registro, mano):
    ## PROVISORIO - MEJORAR IA QUERER RETRUCO DEL OPONENTE
    n = random.randint(0,1)
    if n == 0: return False
    else: return True
    ## PROVISORIO - MEJORAR IA QUERER RETRUCO DEL OPONENTE
    
def querer_vale_cuatro(registro, mano):
    ## PROVISORIO - MEJORAR IA QUERER VALE CUATRO DEL OPONENTE
    n = random.randint(0,1)
    if n == 0: return False
    else: return True
    ## PROVISORIO - MEJORAR IA QUERER VALE CUATRO DEL OPONENTE
    
def irse_al_mazo(registro, mano):
    ## PROVISORIO - MEJORAR IA IRSE AL MAZO DEL OPONENTE
    n = random.randint(0,1)
    if n == 0: return False
    else: return True
    ## PROVISORIO - MEJORAR IA IRSE AL MAZO DEL OPONENTE
    
def esperar_respuesta(mano):
    carta_elegida = random.choice(mano)
    mano.remove(carta_elegida)
    return carta_elegida
	
	
''' TESTS	
for i in range(10):
    b = [("ESPADA",1),("BASTO",1),("ORO",1)]
    print(b)
    print(esperar_respuesta(b))
    print(b)
    print("--------")
    '''
