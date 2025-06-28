import os

# Limpiar pantalla
os.system("cls" if os.name == "nt" else "clear")

# Lista de clientes
clientes = []

# Menú principal
def menu():
    print("\n** MENU **")
    print("1- Ingresar usuario")
    print("2- Buscar usuario")
    print("3- Eliminar usuario")
    print("4- Salir")

# Opción 1: Ingresar usuario
def ingresar_usuario():
    name = input("Ingrese el nombre de usuario: ")

    # Validar género
    while True:
        gender = input("Ingrese el sexo (M/F): ").lower()
        if gender not in ("m", "f"):
            print("Debe ingresar M o F solamente. Intente de nuevo.")
        else:
            print("Sexo confirmado.")
            break

    # Validar contraseña
    while True:
        password = input("Ingrese contraseña: ")
        errores = []
        if not any(char.isdigit() for char in password):
            errores.append("Debe contener al menos un número.")
        if not any(char.isupper() for char in password):
            errores.append("Debe contener al menos una letra mayúscula.")
        if len(password) < 4:
            errores.append("Debe tener al menos 4 caracteres.")

        if errores:
            for e in errores:
                print(f"{e}")
        else:
            print("Contraseña válida.")
            break

    usuario = {
        "Name": name,
        "Gender": gender,
        "Password": password
    }

    clientes.append(usuario)
    print("Usuario ingresado con éxito.")

# Opción 2: Buscar usuario
def buscar_usuario():
    name = input("Ingrese el nombre del usuario a buscar: ")
    encontrado = False
    for cliente in clientes:
        if cliente["Name"].lower() == name.lower():
            print(f"Cliente: {cliente['Name']}, Género: {cliente['Gender']}, Password: {cliente['Password']}")
            encontrado = True
            break
    if not encontrado:
        print("Usuario no encontrado.")

# Opción 3: Eliminar usuario
def eliminar_usuario():
    name = input("Ingrese el nombre del usuario a eliminar: ")
    for cliente in clientes:
        if cliente["Name"].lower() == name.lower():
            print(f" Cliente encontrado: {cliente['Name']}")
            confirmacion = input("¿Desea borrarlo? (s/n): ").lower()
            if confirmacion == "s":
                clientes.remove(cliente)
                print("Usuario borrado correctamente.")
            else:
                print("Usuario no fue borrado.")
            return
    print("Usuario no encontrado.")

# Opción 4: Salir del programa
def salir():
    print("Terminando programa...")

# Bucle principal
while True:
    menu()
    opc = input("Ingrese una opción: ")

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
            print("Opción no válida. Intente de nuevo.")