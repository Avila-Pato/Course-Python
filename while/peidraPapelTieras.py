import random

opciones = ["piedra", "papel", "tijera"]
victorias = 0
derrotas = 0

while True:
    usuario = input("Elige (piedra/papel/tijera) o 'salir': ").lower()
    
    if usuario == "salir":
        break
    
    if usuario not in opciones:
        print("Opción inválida")
        continue
    
    computadora = random.choice(opciones)
    print(f"Computadora eligió: {computadora}")
    
    if usuario == computadora:
        print("Empate")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        victorias += 1
        print("¡Ganaste!")
    else:
        derrotas += 1
        print("Perdiste")

print(f"Victorias: {victorias} | Derrotas: {derrotas}")