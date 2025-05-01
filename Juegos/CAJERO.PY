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
                # Entregar billetes
                for billete in [20000, 10000, 5000, 2000, 1000, 500]:
                    cantidad = cantDinero // billete ## Calcula cuántos billetes de ese valor caben en el monto actual. 
                    ### ejemplo Ejemplo: si cantDinero = 8500 y billete = 2000, entonces 8500 // 2000 = 4
                    if cantidad > 0:
                        print(f"Entregando {cantidad} billete(s) de {billete}")
                        cantDinero %= billete  ## Resta los billetes entregados 
                
        except ValueError:
            print("Ingrese una cantidad válida")

    elif opc == 3:
        print(f"Su estado de cuenta actual es de {EstadoCuenta}")

    elif opc == 4:
        print("Saliendo del cajero...")
        break

    else:
        print("Ingrese una opción válida")
