import os
if os.system("clear") !=0: os.system("cls")
clientes = []


def menu():
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir")


def ingresar_usuario():
    name = input("Ingrese nombre de usuario: ")

    while True:
        sexo = input("Ingrese sexo: ").lower()
        if sexo not in ("f", "m"):
            print("Debe ingresar M o F solamente. Intente de nuevo.")
        else:
            print("Ingresado correctamente ")
            break

    while True:
        contraseña = input("Ingrese contraseña: ")
        errores = []
        if not any(char.isdigit() for char in contraseña):
            errores.append("Debe contener al menos un número.")
        if not any(char.isupper() for char in contraseña):
            errores.append("Debe contener al menos una letra mayúscula.")
        if len(contraseña) <= 4:
            errores.append("Debe tener al menos 4 caracteres.")

        if errores:
            for e in errores:
                print(f"{e}")
        else:
            print("Contraseña válida.")
            break

    usuario = {
        "Name": name,
        "Sexo": sexo,
        "Contraseña": contraseña
    }

    clientes.append(usuario)
    print("Usuario Registrado Correctamente")

def buscar_usuario():
    name = input("Ingrese el nombre del usuario: ")

    encontrado = False
    for cliente in clientes:
        if cliente["Name"].lower() == name.lower():
            print("Usuario encontrado")
            print(f"Nombre:", cliente["Name"], "\nContraseña:", cliente["Contraseña"], "\nSexo:", cliente["Sexo"].upper())
            encontrado = True
            break
        else:
            print("No se encuentra el usuario")
    if not encontrado:
        print("No se encuentra este usuario")

def eliminar_usuario():
    name = input("Ingrese el nombre del usuario a eliminar: ")
    encontrado2 = False
    for cliente in clientes:
        if cliente["Name"] == name.lower():
            print("Usuario encontrado")
            print(f"Nombre:", cliente["Name"], "\nContraseña:", cliente["Contraseña"], "\nSexo:", cliente["Sexo"].upper())
            encontrado2 = True

            while True:
                confirmar = input("Esta seguro que desea borrar el usuario (s/n): ").lower()
                if confirmar == "s":
                    clientes.remove(cliente)
                    print("Usuario borrado correctamente.")
                    break
                elif confirmar == "n":
                    print("Usuario no fue borrado.")
                    break
                else:
                    print("Ingrese una opcion correcta (s/n) ")
            break

    if not encontrado2:
        print("Usuario no fue encontrado")

def salir():
    print("Programa terminado... ")

while True:
    menu()
    try:
        opc = input("Ingrese una opcion: ")

        match opc:
            case "1":
                ingresar_usuario()
            case "2":
                buscar_usuario()
            case "3": 
                eliminar_usuario()
            case "4":
                salir()
                break
            case _:
                print("Ingrese una opcion valida")  
    except:
        print("\nSi desea salir termine con el 4 ")