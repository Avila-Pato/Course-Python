# Pídele al usuario un número y luego usa un for para imprimir la tabla de multiplicar de ese número, desde el 1 hasta el 10.

# Requisitos:
# El usuario ingresa un número.
# Usar for para mostrar la tabla multiplicando del 1 al 10.
# No uses while, solo for.

import os 

if os.system("clear") != 0: os.system("cls")

user = int(input("Ingrese un numero \n"))

for i in range(1, user):
    print(f"{user} X {i } = {user * (i) }")
