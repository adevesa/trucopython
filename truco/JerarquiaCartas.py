## JerarquiaCartas.py

jerarquiaTruco = {("ESPADA",1): 1, ("BASTO",1): 2, ("ESPADA",7): 3, ("ORO",7): 4,
                  ("ESPADA",3): 5, ("BASTO",3): 5, ("COPA",3): 5, ("ORO",3): 5,
                  ("ESPADA",2): 6, ("BASTO",2): 6, ("COPA",2): 6, ("ORO",2): 6,
                  ("COPA",1): 7, ("ORO",1): 7,
                  ("ESPADA",12): 8, ("BASTO",12): 8, ("COPA",12): 8, ("ORO",12): 8,
                  ("ESPADA",11): 9, ("BASTO",11): 9, ("COPA",11): 9, ("ORO",11): 9,
                  ("ESPADA",10): 10,("BASTO",10): 10,("COPA",10): 10,("ORO",10): 10,
                  ("BASTO",7): 11, ("COPA",7): 11,
                  ("ESPADA",6): 12, ("BASTO",6): 12, ("COPA",6): 12, ("ORO",6): 12,
                  ("ESPADA",5): 13, ("BASTO",5): 13, ("COPA",5): 13, ("ORO",5): 13,
                  ("ESPADA",4): 14, ("BASTO",4): 14, ("COPA",4): 14, ("ORO",4): 14 }
                
			
def le_gana_a(*cartas):
    jugadores = len(cartas)
    
    if jugadores == 2: 
        carta1, carta2 = cartas
        if (jerarquiaTruco[carta1] < jerarquiaTruco[carta2]): return "JUGADOR 1"
        elif (jerarquiaTruco[carta1] == jerarquiaTruco[carta2]): return "EMPATE"
        else: return "JUGADOR 2"
    if jugadores == 4:
        carta1, carta2, carta3, carta4 = cartas
        lista = [carta1,carta2,carta3,carta4]
        maximo = 15
        i = 1
        j = i
        repetido = False
        for carta in lista:
            if (jerarquiaTruco[carta] == maximo):
                repetido = True
            
            if (jerarquiaTruco[carta] < maximo):
                maximo = jerarquiaTruco[carta]
                repetido = False
                j = i
            i = i + 1
        if not repetido: return "JUGADOR " + str(j)
        else: return "EMPATE"
    if jugadores == 6:
        carta1, carta2, carta3, carta4, carta5, carta6 = cartas
        lista = [carta1,carta2,carta3,carta4,carta5,carta6]
        maximo = 15
        i = 1
        j = i
        repetido = False
        for carta in lista:
            if (jerarquiaTruco[carta] == maximo):
                repetido = True
            
            if (jerarquiaTruco[carta] < maximo):
                maximo = jerarquiaTruco[carta]
                repetido = False
                j = i
            i = i + 1
        if not repetido: return "JUGADOR " + str(j)
        else: return "EMPATE"
        
    return
   
  
##print(le_gana_a(("ESPADA",1),("ESPADA",1)))
##print(le_gana_a(("ESPADA",2),("ESPADA",4),("ESPADA",1),("ESPADA",6)))
##print(le_gana_a(("ESPADA",4),("ESPADA",2),("ESPADA",3),("ESPADA",4),("ESPADA",1),("ESPADA",6)))