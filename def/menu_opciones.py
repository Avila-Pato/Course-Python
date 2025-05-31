
import os

if os.system("clear") !=0: os.system("cls")


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
        print("Ingrese solo valores numericos")


def opcion_2():

    saldo_tarjeta = 100000 
    total = 0
    
    while True:
        add = (input("Si desea salir ingrese (salir) \n  Ingrese su compra "))
        
        if add == "salir":
            print("saliendo")
            break
        
        try:
            entrada = int(add)
            
            if entrada > 0:
                if entrada <= saldo_tarjeta:
                    total = total + entrada
                    saldo_tarjeta = saldo_tarjeta - entrada
                    print(f"Compra realizada por ${entrada}.")
                    print(f"Saldo restante: ${saldo_tarjeta}\n")
                else:
                    print("Fondos  insuficietes en al tarjeta")
            else:
                print("Ingresa un monto mayor que cero.") 
        except ValueError:
            print("Ingrese valor numerico")        
    
    print(f"Total gastado: ${total}")
    print(f"Saldo final en la tarjeta: ${saldo_tarjeta}")
       
        
def opcion_3():
    print("Saliendo")   
    exit()
    
while True:
    mostrar_menu()
    try:
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
    except Exception :
        print("Ingrese una opcion valida")
  
    
