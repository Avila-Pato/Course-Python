import os

if os.system("clean") != 0:
    os.system("cls")

EstadoCuenta = 0

print("Cajero el --TeRoboSiEntras--")

while True:
    print("Escoja 1 opción")
    try:
        opc = int(input("1> Ingresar dinero\n2> Retirar dinero\n3> Ver dinero\n4> Salir\n"))
    except ValueError:
        print("Ingrese una opción válida")
        continue

    if opc == 1:
        try:
            cantIngresar = int(input("Ingrese la cantidad que desea ingresar\n"))
            if cantIngresar > 0:
                EstadoCuenta += cantIngresar
                print(f"Ingresando {cantIngresar}. Estado de cuenta actual: {EstadoCuenta}")
            else:
                print("Debe ingresar una cantidad positiva")
        except ValueError:
            print("Ingrese un número válido")

    elif opc == 2:
        try:
            cantDinero = int(input("Ingrese la cantidad que desea retirar\n"))
            if cantDinero <= 0:
                print("La cantidad debe ser mayor que cero")
            elif cantDinero > EstadoCuenta:
                print("Fondos insuficientes")
            else:
                EstadoCuenta -= cantDinero
                print(f"Retirando {cantDinero}. Estado de cuenta actual: {EstadoCuenta}")
                for billete in [20000, 10000, 5000, 2000, 1000, 500, 100, 50, 20, 10, 5, 1]:
                    cantidad = cantDinero // billete 
                    if billete == cantDinero or cantidad > 0:
                        cantDinero = cantDinero % billete # %=  me da el residuo de la division 
                        #por ejemplo 10 entre 3 cabe 3 veces y el residuo es 1
                        print(f"Entregando {cantidad} billete(s) de {billete}")


        except ValueError:
            print("Ingrese una cantidad válida")

    elif opc == 3:
        print(f"Su estado de cuenta actual es de {EstadoCuenta}")

    elif opc == 4:
        print("Saliendo del cajero...")
        break

    else:
        print("Ingrese una opción válida")



## // te da cuántos billetes de ese tipo puedes entregar.

## %= te actualiza el valor restante (lo que todavía falta por cubrir con billetes más pequeños).