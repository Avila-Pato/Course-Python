
###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

for idx in range(20):
    if idx % 2 == 0:
        print(idx) 

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]


media = sum(numeros) / len(numeros)
print(f"{media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]
numeroMayor = max(numeros)
print(numeroMayor)

lista = ["ropa", "tele","camisa","nothing"]
lista.sort()
print(lista)


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")


palabra = input("Ingresa una palabra de 4 letras: ")

if len(palabra) == 4:
    for i in range(len(palabra)):
        print(f" {i + 1} {palabra}")
else:
    print("no hay palabras de mas de 4 letras ")

##Array listo

    palabras = ["casa", "arbol", "sol", "elefante", "luna"]


if len(palabra) == 4:
    print("¡Correcto! La palabra tiene 4 letras.")
    for i in range(len(palabra)):
        print(f"Letra {i + 1}: {palabra[i]}")
            
else:
    print("❌ La palabra no tiene 4 letras.")



# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]

letra = input("Ingrese 1 letra ").lower()

contador = 0

for palabra in palabras:
    if palabra.startswith(letra):
        contador += 1
    print(f" Hay  {contador} letra en la {palabra} que empiexa con la letra {letra}")

    
    