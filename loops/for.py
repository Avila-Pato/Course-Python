import os
import random 

if os.system("clear") != 0: os.system("cls")

contador = 0

user = int(input("Ingrese un numero:\n "))

for i in range(user):
    contador += 1
    print(contador)

nombres = ["pepe", "juan", "pedro", "jose"]
for nombre in nombres:
    print(nombre)

carros = ["Audi", "Mercedes", "BMW", "Ferrari"]

for i in range(len(carros)):
    print(carros[0])

#Enumerete

frutas = ["Manzana", "Pera", "Naranja"]

for i, fruta in enumerate(frutas):
    print(f"{i + 1} - {fruta}")

#Bucles anidados

letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras: 
    for numero in numeros:
        print(f"{letra}{numeros}")

#break
print("\nbreak")

animales = ["Perro", "Gato", "Pez", "raton", "conejo"]

for idx, animal in enumerate(animales):
    print(animal)
    if animal == "raton":
        print(f"El raton esta escondido en el indice {idx + 1}")
        break
#continue
print("\n continue")

animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    if animal == "raton": continue
    print(animal)

#Compresion de listas 
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]

animales_Mayusculas = [animal.upper() for animal in animales ] 

print(animales_Mayusculas)


cadena = ["lobo", "cerdo", "serpiente", "caballo"]
leer = random.choice(cadena)

num = len(leer)
print(num)
for i in range(len(leer[0])):
    print(leer[0])