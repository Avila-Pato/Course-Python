import random 

def adivina_numero():
    numero_secreto = random.randint(1, 10)

    print("¡Bienvenido al juego de adivinar el número!")
    print("He elegido un número entre 1 y 10. ¿Puedes adivinar cuál es?")

    intentos = 0
    while True:
        try: 
            adivian = int(input("Introduce tu número: "))
            intentos += 1
            if adivian < 1 or adivian > 10:
                print("Por favor, elige un número entre 1 y 10.")
                continue
            if adivian < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivian > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
                print("Por favor, introduce un número válido")

adivina_numero()                
