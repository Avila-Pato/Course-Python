import random

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
    letra = input("Ingresa una letra: ").lower()

    if letra in palabra:
        # Reemplazar "_" con la letra en posiciones correctas
        for i, l in enumerate(palabra):
            if l == letra:
                progreso[i] = letra
        print("¡Bien! Progreso:", " ".join(progreso))
    else:
        print("Letra incorrecta. Intenta otra vez.")
    
    if "_" not in progreso:
        print("¡Felicidades! Adivinaste la palabra:", palabra)
        break
