# programa de inversionistas 
import math 
# input 

C1 = int(input("introduzca el valor de capital de Juan:" ))
C2 = int(input("ahora introduce el capital de Pedro:" ))
C3 = int(input("capital necesario para hacer el negocio:" ))

meses = 0
# proceso
while C1 + C2 < C3:
    C1 = C1 * 1.03
    C2 = C2 * 1.04
    meses = meses + 1 

print("el negocio se hará en:", meses, "meses")