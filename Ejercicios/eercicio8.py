
# Descripción de la Actividad:


# ETAPAS:
# Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos:
# 1) iniciar sesión
# 2) registrar usuario
# 3) salir
# Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contraseña,
# ambas con valor inicial vacío, ejemplo:
# • usuario1= None
# • usuario2=None
# • usuario3=None
# • contrasena1= None
# • contrasena2=None
# • contrasena3= None
# Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar que
# es necesario registrar un usuario antes, y volverá al menú principal, en el caso de que
# ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente
# menú:
# 1) Realizar llamada
# 2) Enviar correo electrónico
# 3) Cerrar sesión
# 2
# Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar 
# con 9 y su
# tamaño es de 9 dígitos (ejemplo: 985447561).

# La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de
# “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
# También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”


# Finalmente cerrar sesión, volverá al menú principal.
# El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocurre
# esto, entonces el sistema emite un error y vuelve a solicitar la opción.
# Recuerde utilizar try Exception en caso de ser nece

import os

if os.system("clean") != 0: os.system("cls")

numero_guardado = []

while True:
    print("Elija 1 opcion")
    try:
        opc = int(input("\n1)Realizar llamada\n2)Enviar correo electronico\n3)Cerrar sesion\n"))
    except Exception :
        print("Elija una opcion correcta")
        continue
    
    if opc == 1:
        try:
            numero = int(input("Ingrese su numero telefonico"))
            numero_str = str(numero) # pasa a str porque la variable numero es int
            ## ya que el numero ingresado debe ser de 9 digitos y len sirve para contar
            ## los caracteres en este caso porque el numero es de 9 y len solo cuenta
            ## los caracteres
            if numero < 0:
                # print(type(numero))
                print("Ingrese un numero positivo")
            elif len(numero_str) != 9: #aqui cuenta los digitos como caracteres 
                print("el numero debe contenr 9 digitos")
            else:
                print(f"Lammando al numero 9-{numero}..")
                # numero_guardado.append(numero)
                # print(f"Numeros gurdados {"9",numero_guardado}")
        except Exception:
            print("Ingrese un numero valido")
    
    elif opc == 2:
        try:
            correo = str(input("Ingrese su correo electronico "))
            if "@" in correo and  ".com" in correo and len(correo) > 0:
                print(f"Correo electronico valido {correo}")
            else:
                print("Correo electronico no  valido")
        except Exception :
            print("Ingrese un correo electronico valido")
        
    elif opc == 3:
        print("Cerrando sesion...")
        break

    else:
        print("Elija una opcion correcta")
       
