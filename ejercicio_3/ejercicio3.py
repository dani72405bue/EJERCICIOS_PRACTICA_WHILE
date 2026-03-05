# programa de python para adivinar el numero 

import random 
intento = 0
numero = random.randint (1 , 100)

while intento != numero:
    intento = int(input("adivina el numero desde el 1 hasta el 100: "))

    if intento < numero:
        print ("el numero es mas alto")
    elif intento > numero:
        print ("el numeroes mas bajo")

print ("FELICIDADES, HAZ ENCONTRADO EL NUMERO")