
import os 

if os.system("clear") != 0: os.system("cls")

primos = 0
no_primos = 0

try:
    numero = int(input("Ingrese la cantidad de números a verificar: "))
    
    if numero < 0:
        print("Debe ingresar un número positivo.")
        
    
    for i in range(0, numero):
            try:
                num = int(input("Ingrese número: "))
                if num % 2 == 0:
                    print("Es primo.")
                    primos += 1
                elif num % 2 == 1:
                    print("No es primo.")
                    no_primos += 1
                else:
                    print("Debe ingresar un valor valido.")
            except:
                print("Debe ingresar un número entero.")
except:
    print("Debe ingresar un número entero.")
    
    
if primos > 0 or no_primos > 0:
        print(f"Se ingresaron {primos} números primos.")
        print(f"Se ingresaron {no_primos} números no primos.")
   