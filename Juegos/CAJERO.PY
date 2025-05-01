# debe ingresar a un cajero e indicar el dinero a retirar del programa debe indicar cuantos billetes de cada numeracion debe entragar

import os

if os.system("clean") !=0: os.system("cls")
EstadoCuenta = 0 

print("Cajero el --TeRoboSiEntras--")

while True:  

    print("Escoja 1 opcion")
    opc = int(input("1> Ingresar dinero\n2> Retirar dinero \n3> Ver dinero\n4> Salir\n"))

    if opc == 1:
        cantIngresar = int(input("Ingrese la cantidad que desea ingresar\n"))
        if cantIngresar > 0:
            EstadoCuenta += cantIngresar
            print(f"Ingresando {cantIngresar} su estado de cuenta actual es de {EstadoCuenta}")
    elif opc == 2: 
        cantDinero = int(input("Ingrese la cantidad que desea retirar\n"))
        if cantDinero <= EstadoCuenta:
            EstadoCuenta -= cantDinero
            print(f"Retirando {cantDinero} su estado de cuenta actual es de {EstadoCuenta}")
    elif opc == 3:
        print(f"Su estado de cuenta actual es de {EstadoCuenta}")
    elif opc == 4:
        print("Saliendo del cajero...")
        break
    else:
        print("Ingrese 1 opcion valida")




