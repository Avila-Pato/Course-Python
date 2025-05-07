# Una empresa de transporte requiere automatizar sus procesos de cálculo para poder cobrar
# por la cantidad de paquetes que trae un cliente.
# Para calcular el valor total a cobrar y catalogarlo para envío, requiere preguntar el peso de
# cada bulto y determinar el valor según lo siguiente:

# Ejemplo:
# Si un cliente ingresa 3 bultos y según sus pesos estos clasifican en 1 liviano y 2 normales, el
# cliente debe paga $5,000

# El sistema debe mostrar lo siguiente:
# 1 bulto liviano $1,000
# 2 bultos normales $4,000
# Valor total a pagar: $5,000

import os

if os.system("clear") != 0:
    os.system("cls")

livianos = 0
normales = 0
numBulto = 0

# Precios
precio_liviano = 1000
precio_normal = 2000

try:
    bultos_cantidad = int(input("Ingrese la cantidad de bultos  \n"))
except ValueError:
    print("Igrese un valor valido")
    exit()


for i in range(1, bultos_cantidad + 1):
    try:
        numBulto += 1
        bultos = float(input(f"Ingrese la cantidad del primer {numBulto} bultos peso valido entre (1kg a 10kg) "))
    except ValueError:
        print("Ingrese un valor valido (1kg a 10kg)")
        break
        # continue // Puede hacer esata opcion cointunue para que a pesar de haverse equivocado puede seguir el proceso

    if 1 <= bultos <= 5:
        livianos += 1
    elif 6 <= bultos <= 10:
        normales += 1
    else:
        print("No valido ingrese un numero entre (1kg a 10kg)")

total = (livianos * precio_liviano) + (normales * precio_normal)

print(f"{livianos} bultos Livianos : precio  {livianos * precio_liviano}" )
print(f"{normales} bultos Grandes : precio  {normales * precio_normal}" )

print(f"total a  pagar {total}")

