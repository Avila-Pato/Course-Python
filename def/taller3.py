
# 1. Solicitar al usuario que ingrese una lista de números enteros
# separados por espacios.

# 2. Implementar una función llamada validar_lista_numeros que verifique
# que todos los elementos ingresados sean números enteros. Si se
# ingresa algún valor no válido, solicitar nuevamente la lista.

# 3. la función validar_lista_numeros debe utilizar un bucle y maneja
# excepciones para asegurar que todos los elementos ingresados sean
# números enteros.
# 
# 4. Utilizar el operador de módulo % (MOD) para determinar si un
# número es par o impar en la lista de números a ingresar. Considerar
# que un número es par cuando el mod es igual a 0, en caso contrario,
# es impar

# 5. Crear dos listas separadas: una para los números pares y otra para
# los impares.

# 6. Mostrar al usuario las listas resultantes, indicando los números
# pares, e indicando los números impares

import os

if os.system("clear") !=0: os.system("cls")


lista_numeros = []
def menu():
    print("1)Ingrese un numero entero ")
    


def opc1():
    flag = True
    while flag:
        try:   
            numero = int(input("1)Ingrese un numero entero \n2)Si desea ver su lista de numeros "))
            if numero == 1:
                numero = int(input("ingrese un numero")) 
                lista_numeros.append(numero)
                print("Numero ingresado corerctamente")
                flag= False
            elif numero == 2:
                if len(lista_numeros) == 0:
                    print("Su lista se encuentra vacia")
                else:
                    for n in lista_numeros:
                        print(f" su lista de numeros es {n}")
            else:
                print("Ingrese un valor valido")
        except:
            print("ingrese un valor valido")
def opc2():
    print("Hola que hace")


while True:
    menu()
    opc = input("Ingrese una opcion \n")  
    match opc:
        case "1":
            opc1()
        case "2":
            opc2()
        case _:
            print("Ingrese un valor valido")
            


   
    
