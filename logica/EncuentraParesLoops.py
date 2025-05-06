# Desarrolle un programa que reciba 3 números por teclado, uno por uno, y diga: cuántos números son pares y cuantos impares. 
# Además, debe indicar si la suma de todos los números es mayor a 100. Si lo es, debe indicar si la suma es par o impar.  

# Ejemplo 1: 

# Ingrese numero: 20 
# Ingrese numero: 4 
# Ingrese numero: 10 
# Se ingresaron 3 números pares. 
# Se ingresaron 0 números impares. 
# La suma no es mayor a 100. 

import os 

if os.system("clear") != 0: os.system("cls")

num1 = int(input("Ingrese el primer numero \n"))
num2 = int(input("Ingrese el segundo numero \n"))
num3 = int(input("Ingrese el tercer numero \n"))
# Inicialización de contadores
par = 0
impar = 0
numeros = [num1, num2, num3]

# Conteo de pares e impares
for num in numeros:
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

# Mostrar resultados
print("-----------------------------------------")
print(f"Se ingresaron {par} números pares.")
print(f"Se ingresaron {impar} números impares.")


