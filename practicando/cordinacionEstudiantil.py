
import os

if os.system("clear") !=0: os.system("cls")

usuarios = []

pregunta = str(input("Desea ingresar aa un usuario (si/no)"))

while pregunta == "si":

    nombre = str(input("Ingrese su nombre: \n"))
    direccion = str(input("Ingrese su dirreccion: \n"))
    telefono = str(input("Inrese su numero telefonico: \n"))

    #Diccionario guardaare lista de usuarios
    usuario = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono
    }

    usuarios.append(usuario)

    pregunta = str(input("Desea ingresar otro? \n"))

    while pregunta not in ("si", "no"):
        print("Inrese un opcion valida")
        pregunta = input("¿Desea ingresar otro usuario? (s/n): ")


for alumnos in usuarios:
    print("Nombre", alumnos["nombre"])
    print("direccion", alumnos["direccion"])
    print("Telefono", alumnos["telefono"])
    print("")
