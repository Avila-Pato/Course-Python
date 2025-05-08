# Deberás construir un programa que esta diseñado para ayudar en la venta
# de pasajes. Inicia preguntándote cuántos pasajes deseas vender. Luego,
# utiliza un proceso organizado (llamado bucle for) para pedirte el precio de
# cada pasaje por separado. Si ingresas un valor que no es un número, te
# indica que necesitas proporcionar un valor numérico válido. Al final, muestra
# el monto total que se ha obtenido por la venta de todos los pasajes

# • Solicita al usuario la cantidad de pasajes a vender.
# • Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
# • Dentro del bucle, se solicita al usuario el precio de cada pasaje y se
# acumula en la variable totalIngresos.
# • Si el usuario ingresa un valor no numérico para el precio del pasaje,
# el programa muestra un mensaje y sale del bucle usando break.
# • Finalmente, se imprime el total de ingresos por la venta de pasajes

import os

if os.system("clear") !=0: os.system("cls")


boletos = 0
totalIngresos = 0

try:
    pasajes_vendidos = int(input("Ingrese la cantidad de boletos a vender: "))
except ValueError:
    print("Por favor, ingrese un número válido.")
    exit()

for i in range(1, pasajes_vendidos + 1):
    try:
        boletos += 1
        precio_boleto= int(input(f"Ingrese el precio del boleto {boletos} \n"))
        totalIngresos =+ precio_boleto * boletos
    except ValueError:
        print("Ingrese un valor valido")
        break

print(f"El total de ingresos es ${totalIngresos:.2f} dolares")

## :2.f define como valor float 

   