# PROGRAMA EN PYTHON PARA PONER LA CONTRASEÑA CORRECTA

contraseña = input("bienvenido, inserte la contraseña dada por el instructor: ")

while contraseña != "python123":
    print("la contraseña es incorrecta")
    contraseña = input("ingrese nuevamente: ")

print("la contraseña es correcta")