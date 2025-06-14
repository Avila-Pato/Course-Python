# Ejercicio Adicional 3: Tuplas y Conjuntos en Combinación
# Creen un programa que solicite a los usuarios ingresar nombres y edades.
# # Almacenen estos datos en un diccionario. Luego, imprima solo las edades
# # de los usuarios.

usuarios = {} # esto es un diccionario
# usuarios = [] # esto es una lista

while True:
    nombre = input("Ingrese el nombre del usuario (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    edad = int(input("Ingrese la edad del usuario: "))
    # Almacena el nombre y la edad en el diccionario
    usuarios[nombre] = edad # Almacena el nombre y la edad en el diccionario segun la llave osea el nombre por ejemplo si llamo a alguien pato lo guardo en el diccionario con la llave pato y su edad

print("Edades de los usuarios:")
for nombre, edad in usuarios.items(): #usuarios.items() devuelve una lista de tuplas (llave, valor)
    # ene ste caso la llave es el nombre y el valor es la edad
    print(f"{edad}")