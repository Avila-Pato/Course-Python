# La empresa de juegos de azar “Lotín”, desea crea una aplicación
# móvil que genere sorteos rápidos dentro del mismo celular.
# Para eso, le solicita crear un algoritmo que genere una lista de
# números de manera aleatoria donde si usted acierta, gana. Las
# reglas son las siguientes:
# • Los números participantes son del 1 al 49
# • El jugador debe elegir 7
# • Se generarán 3 rondas de conjunto de números ganadores
# • Si el jugador acierta a una de las 3 ronda, gana
# Programe las líneas de código faltantes

import os
import random

if os.system("clear") != 0:
    os.system("cls")

listaNumeros = []
intentos = 3


print("Ingrese sus 7 numeros de la suerte:  ")
while intentos > 0:
    ramdomNumero = random.randint(1, 49)

    for i in range(1, 8):
        num = int(input(f"Ingrese el numero {i}: "))
        listaNumeros.append(num)

    print(f"Usted ingreso los siguientes numeris {listaNumeros}")

    numeros_sorteo = random.sample(range(1, 50), 7)

    print(f"Los numeros soeteados en la ronda {intentos} son: {numeros_sorteo}")

    if listaNumeros == numeros_sorteo:
        print("Felicidades usted gano")
    else:
        print("Lo siento, usted no gano")
    intentos -= 1


# if intentos == 0:
#     print("Se te dara solo 1 oportunidad mas")
#     ultimoIntento = input(f"Ingrese su ultimo intento")
#     if ultimoIntento == "1234":
#         print("Acceso concedido")
#     else:
#         print("acceco bloqueado")
