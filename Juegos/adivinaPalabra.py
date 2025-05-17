import random
import os

# Limpiar pantalla
if os.system("clear") != 0:
    os.system("cls")

# Lista de palabras
cadena = ["cerdo", "loro", "ballena", "langosta"]

# Elegir palabra aleatoria
palabra = random.choice(cadena)

# Crear progreso con "_" por cada letra
progreso = ["_"] * len(palabra)

# Mostrar progreso inicial
print("Palabra a adivinar:", " ".join(progreso))

# Simular intentos del usuario
while "_" in progreso:
    letra = input("Ingresa una letra o intenta adivinar toda la palabra: ").lower()

    if letra == palabra:
        print("¡Lo lograste! La palabra era:", palabra)
        progreso = list(palabra)  # Mostrar la palabra completa
        break
    elif letra in palabra:
        for i, l in enumerate(palabra):
            if l == letra:
                progreso[i] = letra
        print("¡Bien! Progreso:", " ".join(progreso))
    else:
        print("Inténtalo de nuevo.")

# Verificar si se adivinó por letras
#si ya no hay mas "_" en la letra que esta adivinando significa que el usuario adivino toda la palabra
if "_" not in progreso:
    print("¡Felicidades! Adivinaste la palabra:", palabra)
