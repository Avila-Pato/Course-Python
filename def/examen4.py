import os
if os.system("clear") !=0: os.system("cls")
clientes = []
import random
import string

def menu():
    print("1.- Comprar entrada. ")
    print("2.- Consultar Comprador. ")
    print("3.- Cancelar Compra. ")
    print("4.- Salir. ")

def comprar_entrada():
    nombre = input("Ingrese el nombre del comprador: ")
    entrada = input("Ingrese tipo de entrada (G/V): ").lower()

    if entrada not in("g", "v"):
        print("Tipo den entrada no valida")
        return
    
    if any(cliente["Nombre"] == nombre for cliente in clientes):
        print("Ya se  encuentra este usuario ")
        return

    else:
        codigo_confirmacion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        print(f"Codigo de confirmacion {codigo_confirmacion}")
        
        flag = True
        while flag:
                try:    
                    codigo = (input("Ingrese el codigo de confirmacion: ")).upper().strip()
                    # Strip() elimina los espacion en blanco

                    if  codigo == codigo_confirmacion:
                        flag = False
                        print("Codigo verificado correctamente ")
                    else:
                        print("Codigo no valido ingrese nuevamente ")
                except:
                    print("Cogido no  valido")        

    usuario = {
        "Nombre": nombre,
        "Codigo": codigo,
        "Contraseña": entrada,
    }
    clientes.append(usuario)
    

def consultar_comprador():

    name = input("Ingrese el nombre del comrpador: ")
    encontrado = False
    for cliente in clientes:
        if cliente["Nombre"].lower() == name.lower():
            print(f"✅ Cliente encontrado:\nNombre: {cliente['Nombre']}\nCódigo: {cliente['Codigo']} \nTipo de Entrada: {cliente['Contraseña'].upper()}")
            encontrado = True
        else:
             print("Cliente no encontrado")
    if not encontrado:
            print("Uusuario no encontrado")
   

def cancelar_compra():
    name = input("Ingrese el nombre del comrpador: ")
    encontrado2 = False
    for cliente in clientes:
        if cliente["Nombre"].lower() == name.lower():
            print(f"✅ Cliente :\nNombre: {cliente['Nombre']}\nCódigo: {cliente['Codigo']}")
            encontrado2 = True

            while True:
                confirmacion = input("Esta seguro que desea cancelar la compra (s/n): ")
                if confirmacion == "s":
                    clientes.remove(cliente)
                    print("Compra Cancelada Con exito")
                    break
                elif confirmacion == "n":
                    print("Compra no Cancelada con exito")
                    break
                else:
                    print("Ingrese una opcion correcta (s/n)")
            break

    if not encontrado2:
        print("Uusario no encontrado")

def salir():
    print("Programa terminado... ")


while True: 
    menu()
    try:
        opc = input("Ingrese una opcion: ")
        match opc:
            case "1":
                comprar_entrada()
            case "2":
                consultar_comprador()
            case "3":
                cancelar_compra()
            case "4":
                salir()
                break
            case _:
                print("Ingrese una opcion correcta ")
    except:
        print("Ingrese una opcion correcta ")
    