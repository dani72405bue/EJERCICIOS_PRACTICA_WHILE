# PROGRAMA DE PYTHON PARA EL DESCENSO DE UNA PELOTA AL REBOTAR

# input

import math
h = int(input("ingresa la altura inicial"))

limite = h/5
altura = h
rebotes = 0

# proceso

while altura>=limite:
    altura = altura * 0.9
    rebotes = rebotes + 1 

# output

print("la cantidad de rebotes dados hasta llegar a la quinta parte son:", rebotes)
