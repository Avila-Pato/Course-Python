import os

if os.system("clear") !=0: os.system("cls")

clientes = []

import random

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
        print("Ya se  encuentras este usuario ")
        return
    else:
        codigo_confirmacion = random.randint(100,999)
        print(f" Codigo de confirmacion {codigo_confirmacion}")
        
        flag = True
        while flag:
                codigo = int(input("Ingrese el codigo de confirmacion: "))

                if  codigo == codigo_confirmacion:
                    flag = False
                    print("Codigo verificado correctamente ")
                else:
                    print("Codigo no valido ingrese nuevamente ")
                

    usuario = {
        "Nombre": nombre,
        "Codigo": codigo,
        "Contraseña": entrada,
    }
    clientes.append(usuario)
    

def consultar_comprador():
    name = input("Ingrese el nombre del comrpador: ")

    for cliente in clientes:
        if cliente["Nombre"].lower() == name.lower():
            print(f"✅ Cliente encontrado:\nNombre: {cliente['Nombre']}\nCódigo: {cliente['Codigo']} \nEntrada: {cliente['Contraseña']}")
        else:
             print("Cliente no encontrado")
   

def cancelar_compra():
    name = input("Ingrese el nombre del comrpador: ")

    for cliente in clientes:
        if cliente["Nombre"].lower() == name.lower():
            print(f"✅ Cliente :\nNombre: {cliente['Nombre']}\nCódigo: {cliente['Codigo']}")
            confirmacion = input("Esta seguro que desea cancelar la compra: ")
            if confirmacion == "s":
                clientes.remove(cliente)
                print("Compra Cancelada Con exito")
            else:
                print("Ingrese una opcion correcta")
        else:
             print("Cliente no encontrado")

def salir():
    print("Programa terminado... ")


while True: 
    menu()
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

    