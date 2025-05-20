
import os

if os.system("clear") !=0: os.system("cls")

# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:

# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.

# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.

# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados.

# .0f	Sin decimales	f"{1000000:.0f}" → 1000000
# .2f	2 decimales	f"{1234.5:.2f}" → 1234.50
# :,.0f	Con separador de miles	f"{1000000:,.0f}" → 1,000,000
# :,.2f	Con miles y 2 decimales	f"{1234567.89:,.2f}" → 1,234,567.89

# print(f"{numero:,.0f}".replace(",", ".")) para cambiar la "," por u "."



def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. Tarjeta  de credito")
    print("2. Carrito de compras")
    print("3. Salir")

def opcion_1():
    deuda = 100000
    print(f"{deuda:,.0f}".replace("," ,"."))
    print(f"su deuda es ${deuda:,.0f}")   
    
    try:    
        deposito_tarjeta = int(input("Ingrese la cantidad de dinero que quiere depositar \n"))

        if deposito_tarjeta < 0:
            print("Ingrese un monto válido (no negativo).")
        elif deposito_tarjeta < deuda:
            saldo_restante = deposito_tarjeta - deuda
            print(f"gracias por el abono tu nuevo saldo es ${abs(saldo_restante):,.0f}")
        elif deposito_tarjeta == deuda:
            print(" has saldado tu deuda")
        else:
            vuelto = deposito_tarjeta - deuda
            print(f"Deuda saldada. Tu vuelto es de ${vuelto:,.0f}.")
        
    except ValueError:
        print("Ingrese solo valoresnumericos")
    
    
def opcion_2():
    print("Carrito de comptras")   
     
def opcion_3():
    print("Salienndo")   
    exit()
    
while True:
    mostrar_menu()
    opc = input("Ingrese una opcion: ")
    
    match opc:
        case "1":
           opcion_1()
        case "2":
            opcion_2()
        case "3":
            opcion_3()
        case _:
            print("")
            print("Ingrese una opcionn valida")
    
    