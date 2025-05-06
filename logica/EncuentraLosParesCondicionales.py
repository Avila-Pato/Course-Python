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

if os.system("clear") !=0: os.system("cls")


sum1= 0
sum2= 0
sum3= 0

impar1= 0
impar2= 0
impar3= 0

num1 = float(input("Ingrese el primer numero \n"))
num2 = float(input("Ingrese el segundo numero \n"))
num3 = float(input("Ingrese el tercer numero \n"))

#Logica
if num1 % 2 == 0:
    sum1 += sum1 + 1
else:
    impar1 += impar1 + 1
    
if num2 % 2 == 0:
    sum2 += sum2 + 1
else:
   impar2 += impar2 + 1

if num3 % 2 == 0:
    sum3 += sum3 + 1
else:
    impar3 += impar3 + 1
    

total_cantidad = (num1 + num2 + num3)
total_pares = (sum1 + sum2 + sum3)
total_impares = (impar1 + impar2 + impar3)


print(f"El numero total de pares es {total_pares}")
print(f"El total de numeros impares es de {total_impares}")

#cONDICIONAL!!
if total_cantidad > 100:
    print("La suma es mayor a 100.")
else:
    print("La suma no es mayor a 100 ")

