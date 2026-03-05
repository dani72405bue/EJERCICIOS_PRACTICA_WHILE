# Programa de python para la vida de un personaje guerrero

import random 

vida = 50

while vida > 0:
    daño=random.randint(1 , 15)
    vida = vida - daño 
    print ("el jefe te quitó:", daño, "de vida")
    print ("vida restante:", vida)

    if vida<0:
        print ("tu vida ha llegado a 0, perdiste la partida")
        break