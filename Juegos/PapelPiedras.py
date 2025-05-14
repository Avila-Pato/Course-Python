import random
import os

# Limpiar pantalla
if os.system("clear") != 0:
    os.system("cls")

opc = ["papel", "piedra", "tijeras"]

intentos = 0
maxIntentos = 3

puntos1 = 0
puntos2 = 0
empate = 0

while intentos < maxIntentos:
    intentos += 1  #Incrementar los intentos para que no entre en un bucle
    
    jugador1 = random.choice(opc)
    jugador2 = random.choice(opc)

    if  (jugador1 == "piedra" and jugador2 == "tijeras") or \
        (jugador1 == "papel" and jugador2 == "piedra") or \
        (jugador1 == "tijeras" and jugador2 == "papel"):
        puntos1 += 1
        print("→ Gana Jugador 1")
    elif jugador1 == jugador2:
        empate += 1
        print("→ Empate")
    else:
        puntos2 += 1
        print("→ Gana Jugador 2")

if puntos1 > puntos2:
        print(f"Jugador 1 a ganado en {puntos1} intentos")
elif puntos2 > puntos1:
        print(f"Juador 2 a ganado en {puntos2} intentos")
else:
        print("LLa partida termina en empate")
