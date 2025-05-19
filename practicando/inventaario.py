
import os

if os.system("clear") !=0: os.system("cls")

productos = []
pregunta = str(input("Desea agregar un nuevo producto:(si/no) \n"))

while pregunta == "si":

    nombreProducto = (input("Ingrese el nombre del producto"))
    categoria = (input("Ingrese el categoria del producto"))
    try:
        precio = float(input("Ingrese el precio del producto"))
        if precio < 0:
            print("el precio debe ser mayor a 0")
    except Exception as e:
        print("Ingrese un numero valido")
        break
    # end try

    ##Diccionario con ={}
    producto = {
        "nombreProducto": nombreProducto,
        "categoria": categoria,
        "precio": precio
    }
    
    productos.append(producto)

    pregunta = str(input("Desea ingresar otro (si/no)? \n"))

    while pregunta not in("si", "no"):
        print("Inrese (si/no) ")
        pregunta = str(input("Desea ingresar otro (si/no)? \n"))
 
for pro in productos:
    print("el producto es", pro["nombreProducto"])
    print("su categoria es", pro["categoria"])
    print("su precio es $", pro["precio"])
    print("")

while pregunta in("no"):
        print("Cerrando programa")
        break
