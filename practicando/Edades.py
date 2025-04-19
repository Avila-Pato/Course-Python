
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
import os

if os.system("clear") != 0: os.system("cls")

print("Clasificacion de edades")

try: 
    edad = int(input("Ingrese una edad:\n"))

    if edad >= 0 and  edad <= 2:
        print("Es un bebe")
    elif edad >= 3 and edad <= 12:
        print("Es un niño")
    elif edad >= 13 and edad <= 17:
        print("es un adolecente")
    elif edad >= 18  and edad <= 64:
        print("Es un adulto")
    else:
        print("Es un adulto mayor")

except ValueError:
    print("Por favor, ingrese un valor numérico")