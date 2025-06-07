# Ejercicio 1 (3 puntos)
# Construya un programa en Python que permita registrar los pacientes de una
# clínica y verificar si cada uno tiene más de 60 años de edad.

# Primero se debe ingresar la cantidad de pacientes a registrar. Este número debe
# ser entero.

# Luego, para cada paciente, se debe pedir su nombre y su edad.
# El programa debe indicar si el paciente tiene “60 años o menos&quot; o “Mayor de 60
# años&quot;.

# Al finalizar, se debe mostrar cuántos pacientes tienen más de 60 años de
# antigüedad y cuántos no.

# Todos los datos numéricos deben validarse con manejo de excepciones.

# paciente_lista = []
# pacientes_mayores_lista = []
# def menu():
#     print("=======================")
#     print("1) Ingresar paciente")
#     print("2) Mostrar Resumen")
#     print("3) Salie")


# def ingresar_pacientes():
#     edad = int(input("Ingrese la edad del paciente"))


#     if edad <= 0:
#         print("Ingrese un valor positivo o que sea mayor a 0")
#     elif edad < 60:
#         paciente = input("Ingreese el nombre del paciente ")
#         print("Paciente registrado Correctamente")
#         paciente_lista.append(paciente)

#     elif edad > 60:
#         pacientes_mayores = input("Ingrese el nombre de la persona arriba de 60 anos")
#         print("Paciente de 60 para arriba  registrado Correctamente")

#         pacientes_mayores_lista.append(pacientes_mayores)
#     else:
#         print("ingrese un valor valido")


# def mostrar_resumen():
#     if not paciente_lista and not pacientes_mayores_lista:
#            print("Por el momento no tiene personas ")
#     else:

#         for pacientes in paciente_lista:
#             print(f"Pacientes menos de 60 anos {len(pacientes)}")

#         for pacientes_mayores in pacientes_mayores_lista:
#             print(f"Pacientes mayores de 60 anos {len(pacientes_mayores)}")


# def salir_game():
#     print("Saliendo...")

# while True:
#     menu()
#     try:
#         opc = int(input("Ingrese 1 opcion \n"))

#         match opc:
#             case 1:
#                 ingresar_pacientes()
#             case 2:
#                 mostrar_resumen()
#             case 3:
#                 salir_game()
#                 break
#             case _:
#                 print("Ingrese una opcion valida")
#     except:
#         print("Ingrese solo 1 de las opciones")


# lista_arriba = []
# lista_mayorees = []

# while True:
#     opc = int(input("\n1) Ingresar usuario\n 2) Ver Resumen 3) Salir "))

#     if opc == 1:
#         edad = int(input("Ingrese la edad del paciente"))

#         if edad <= 0:
#             print("Ingrese un valor pisitiovo o maoyr a 0")
#         elif edad < 60:
#             nombre = input("Ingrese la edad de la persona ")

#             lista = {"Nombre": nombre, "Edad": edad}
#             lista_arriba.append(lista)

#         elif edad > 60:
#             nombre_mayores = input("Ingrese la edad de la persona sobre 60 anos ")

#             lista_mayores_up = {"Nombre": nombre_mayores, "Edad": edad}
#             lista_mayorees.append(lista_mayores_up)

#     elif opc == 2:
#         if not lista_arriba and not lista_mayorees:
#             print("No tiene ninguna persoan registrada")
#         else:
#             for lista_normal in lista_arriba:
#                 print(f"lsita de personas menos de 60 {lista_normal}")
#             for lista_mayor in lista_mayorees:
#                 print(f"lsita de personas mayores de 60 {lista_mayor}")

#             print(f"total de personas menos a 60 {len(lista_arriba)}")
#             print(f"total de personas menos a 60 {len(lista_mayorees)}")

        
#     elif opc == 3:
#         print("Saliendo")
#         break

# La opción 1 debe permitir ingresar un número entero entre 0 y 100. El usuario puede
# ingresar cualquier valor, por lo que debe hacer uso de manejo de excepciones, ya que
# incluso podría ingresar un string en vez de un número. Si el usuario no ingresa un número
# entero, el programa debe entregar el mensaje: &quot;Debe ingresar un número entero!!&quot;, y repetir
# la solicitud de ingreso de número. Si se ingresa un número entero, pero no está dentro del
# rango [0,100] entonces debe mostrar el mensaje: &quot;Debe ingresar un número entre 0 y 100!!&quot;
# y repetir la solicitud de ingreso de número. Si se ingresa un número que cumpla las
# condiciones, entonces debe mostrarse el mensaje: &quot;Ingreso exitoso&quot;.

# La opción 2 debe mostrar el número mayor ingresado hasta ese momento.

# La opción 3 debe mostrar el número menor ingresado hasta ese momento.

# Para ambas opciones, si no se han ingresado números, y se pido el número mayor o menor,
# entonces el programa debe mostrar el mensaje: &quot;No se han ingresado números.&quot;

# La opción 4 permite terminar el programa, mostrando por pantalla el mensaje: &quot;Fin del
# programa. Adiós.&quot;

# En el menú principal, si se ingresa cualquier otro valor que no sea el de las opciones
# mostradas, el programa debe mostrar el mensaje: &quot;Debe ingresar una opción válida.”, y
# volver a preguntar por una opción.
# A continuación, se muestra un ejemplo de ejecución:


lista_numeros = []
def menu():
    print("ingresar un número entero entre 0 y 100")
    print("mostrar el número mayor ingresado")
    print("mostrar el número menor ingresado")
    print("Salir")
    
def ingresar_numero():
    num = int(input("Ingrese un numero"))
    if num <= 100:
        print("Numero Ingresado Correctamente")
        lista_numeros.append(num)
    elif num > 100:
        print("Ingrese un numero menor a 100")
    else:
        print("Ingrese un valor valido")
def mostrar_mayor():
    numero_mayor = max(lista_numeros)
    print(f"El numero mayopr de la lista es {numero_mayor}")

def mostrar_menor():
    numero_menor = min(lista_numeros)
    print(f"El numero menor de la lista es {numero_menor}")
    
def salir():
    print("Saliendo..")
    
while True:
    menu()
    
    try:
        opc = int(input("Elija 1 opcion"))
        
        match opc:
            case 1:
                ingresar_numero()
            case 2:
                mostrar_mayor()
            case 3:
                mostrar_menor()
            case 4:
                salir() 
                break
            case _:
                print("Ingrese un numero de la lista")       
        
    except:
        print("Ingrese un valor valido")
