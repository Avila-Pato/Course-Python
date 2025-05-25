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
bultos = 0

# Precios
precio_liviano = 1000
precio_normal = 2000

bultos_cantidad = 0

while bultos_cantidad <= 0:
        try:    
            bultos_cantidad = int(input("Ingrese la cantidad de bultos  \n"))
            if bultos_cantidad < 0:
                print("Ingrese un numero no negatico")
        except ValueError:
            print("Igrese un valor valido")


for i in range(0, bultos_cantidad, 1):
    peso_valido = False

    while not peso_valido:
        try:
            bultos = float(input(f"Ingrese la cantidad del primer {i + 1} bultos peso valido entre (1kg a 10kg) "))
            if bultos < 0:
                print("Ingrese un pesoo positivo ")
        except ValueError:
            print("Ingrese un valor valido (1kg a 10kg)")

        if 1 <= bultos <= 5:
            livianos += 1
            peso_valido = True
        elif 6 <= bultos <= 10:
            normales += 1
            peso_valido = True
        
            

total = (livianos * precio_liviano) + (normales * precio_normal)

print(f"{livianos} bultos Livianos : precio  {livianos * precio_liviano}" )
print(f"{normales} bultos Grandes : precio  {normales * precio_normal}" )

print(f"total a  pagar {total}")

