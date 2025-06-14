# EJERCICIO 2 Conjunto números primos

# Desarrollar un programa que indique si un número es primo o no dentro de un rango de
# números . Utilicen un diccionario para almacenar los números primos y una función para
# verificar si un número es primo. (recuerde, algoritmo no es comprobado para todos los
# números primos, solo para los primeros números sirve el siguiente algoritmo

numerosPrimos = []


num = int(input("Ingrese un numero"))

# Bucle externo recorre los numeros emepzando desde el 2
for i in range(2, num):
    #Bucle interno recorre los numeros pares
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        numerosPrimos.append(i)

print(numerosPrimos)

