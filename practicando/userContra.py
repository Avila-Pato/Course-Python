

import os

if os.system("clear") !=0: os.system("cls")

intentos = 3
while intentos > 0:

    contra = input("Ingrese la contraseña: ")
    if contra == "1234":
        print("Acceso concedido")
        exit(
            
        )
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
  
if intentos == 0:
        print("Se te dara solo 1 oportunidad mas")
        ultimoIntento = input(f"Ingrese su ultimo intento")
if ultimoIntento == "1234":
        print("Acceso concedido")
else:
    print("acceco bloqueado")

