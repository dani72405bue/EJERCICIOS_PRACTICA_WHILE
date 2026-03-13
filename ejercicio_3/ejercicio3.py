# programa de python para adivinar el numero 

import random
#input
cn=random. randint(1, 100)
intento = 0
n=1
#processing and output
while intento != cn:
    intento = int(input ("Adivina el número (1-100): "))
    n=n+1

    if intento < cn:
        print( "mas alto: ")
    elif (intento>cn):
        print("mas bajo: ")
    else:
        break

print("LO CONSEGUISTE EN: " +str (n)+str(" intentos"))