import os

# Limpiar pantalla (funciona en Windows y Linux/Mac)
os.system("cls" if os.name == "nt" else "clear")

print("Elija una opción")

usuarios = []
sesion_iniciada = False


while True:
    try:
        opc = int(input("\n1) Iniciar sesión\n2) Registrar usuario\n3) Salir\n> "))
    except ValueError:
        print("Ingrese una opción válida (número).")
        continue

    if opc == 1:
        if len(usuarios) == 0:
            print("No hay usuarios registrados. No puede iniciar sesión.")
        else:
            nombre = input("Ingrese el nombre del usuario: ")
            contra = input(f"Ingrese la contraseña de {nombre}: ")
            
            encontrado = False ##new flag
            for u in usuarios:
                if u["Nombre"] == nombre and u["Contra"] == contra:
                    encontrado = True
                    sesion_iniciada = True
                    break

            if encontrado:
                print("Inicio de sesión exitoso.\n")
                while True:
                    try:
                        sub_opc = int(input("1) Realizar llamada\n2) Enviar correo electrónico\n3) Cerrar sesión\n> "))
                    except ValueError:
                        print("Ingrese una opción válida.")
                        continue

                    if sub_opc == 1:
                        numero = input("Ingrese un número telefónico (9 dígitos): ") 
                        if  len(numero) == 9:
                            print("Número guardado correctamente.")
                        else:
                            print("Ingrese un número válido de 9 dígitos.")
                            
                    elif sub_opc == 2:
                        correo = input("Ingrese su correo electrónico: ")
                        if "@" in correo and ".com" in correo and len(correo) > 0:
                            print("Correo ingresado correctamente.")
                        else:
                            print("Ingrese un correo válido.")
                    elif sub_opc == 3:
                        print("Sesión cerrada. Regresando al menú principal...\n")
                        sesion_iniciada = False
                        break
                    else:
                        print("Seleccione una opción válida.")
            else:
                print("Nombre o contraseña incorrectos.")

    elif opc == 2:
        nombre = input("Ingrese el nombre del usuario: ")
        contra = input(f"Ingrese la contraseña de {nombre}: ")
        
        usuarios.append({"Nombre": nombre, "Contra": contra})
        print("Usuario registrado correctamente.")

    elif opc == 3:
        print("Saliendo del programa..")
        break

    else:
        print("Elija una opción correcta.")
