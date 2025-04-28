import random
import os

# Limpiar pantalla
if os.system("clear") != 0:
    os.system("cls")

# Generar número aleatorio
random_number = random.randint(0, 10)

intentos = 1
print("tienes 5 intentos")
while intentos < 5:
    adivina = int(input("Ingrese un número del 0 al 10: "))
    
    print(f"intento {intentos}")
    intentos += 1
    
    if adivina == random_number:
        print(f"¡Acertaste! El número secreto es {random_number}")
        break
    elif adivina < random_number:
        print("Tu número es mayor que el número secreto.")
    else:
        print("Tu número es menor que el número secreto.")

    if intentos == 5:
        print(f"Has agotado tus intentos. El número secreto era {random_number}.")
