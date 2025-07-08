
# Enunciado 4 : Gestión de Biblioteca 

# Descripción: Este sistema permite gestionar los libros de una biblioteca. Se podrán añadir, consultar, modificar y eliminar libros. Cada libro tendrá un ID único, un título, un autor, un año de publicación y un estado (disponible/prestado). 

# Características Clave: 

# •	Uso de un diccionario para almacenar los libros, donde la clave es el ID del libro. 

# •	Menú interactivo para navegar por las opciones. 

# •	Funciones separadas para cada operación: añadir, consultar, modificar y eliminar. 

# •	Control de errores robusto para entradas inválidas, libros no encontrados y IDs duplicados. 

# •	Ciclos while para el menú principal y for para iterar sobre los libros. 

# •	Decisiones if/elif/else para la lógica del menú y las operaciones. 

# • No se utiliza class, todo se maneja con funciones y estructuras de datos básicas. 
import os

if os.system("clear") != 0: os.system("cls")


libros = {}

def menu():
    print("1. Añadir libro")
    print("2. Consultar libro")
    print("3. Modificar libro")
    print("4. Eliminar libro")
    print("5. Salir")
    
def añador_libro():
    # Cada libro tendrá un ID único, un título, un autor, un año de publicación y un estado (disponible/prestado). 
    try:
        id = int(input("Ingrese el id del libro"))
    except:
        print("Ingrese un numero de referencia ")
    
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")   
    
    try:
        año_publicacion = int(input("Ingrese el año de publicacion del libro: "))
    except:
        print("Ingrese un año de referencia")
    while True:
            estado = input("Ingrese el estado del libro: (disponible/prestado)").lower()
            
            if estado in['prestado', 'disponible']:
                print(f"Agregado Correctamente estado {estado}")
                break
            else:
                print("Ingrese solo (disponible/prestado) ")
            
    libros[id] = {
        "Titulo": titulo,
        "Autor": autor,
        "Año": año_publicacion,
        "Estado": estado,
    }        
def consultar_libro():
 
    if not libros:
        print("No se encuentran datos")
        return
    
    idx = int(input("Ingrese el id del libro : "))
    
    encontrado = False
    for id, libro in libros.items():
        if id == idx:
            print(f"ID - {id}")
            print(f"Nombre - {libro['Titulo']} ")
            print(f"Autor - {libro['Autor']}")
            print(f"Año - {libro['Año']} ")
            print(f"Estado - {libro['Estado']}")
            encontrado = True
    if not encontrado:
        print("No se encuentra esta ID")
        
def modificar_libro():
       
    if not libros:
        print("No se encuentran datos")
        return
    
    idx = int(input("Ingrese el id del libro que desea modificar : "))
    
    for id, libro in libros.items():
        if id== idx:
            print(f"Titulo = {libro['Titulo']}")
            print(f"Autor - {libro['Autor']}")
            print(f"Año - {libro['Año']} ")
            print(f"Estado - {libro['Estado']}")
            
            libro['Titulo'] == input("Nuevo Titulo: ")
            libro['Autor'] == input("Nuevo Autor: ")
            libro['Año'] == int(input("Nuevo Año:  "))
            libro['Estado'] == input("Nuevo Estado: ")

            print("Actualizado correctamente ")
        else:
            print("Ingrese una opcion correcta")
def eliminar_libro():
    if not libros:
        print("No se encuentran datos")
        return

    idx = int(input("Ingrese el id del libro que desea borrar: "))

    for id, libro in libros.items():
        if int(id) == idx:
            print(f"Título: {libro['Titulo']}")
            print(f"Autor: {libro['Autor']}")
            print(f"Año: {libro['Año']}")
            print(f"Estado: {libro['Estado']}")

            confirmar = input("¿Está seguro que desea eliminarlo? (s/n): ").lower()

            if confirmar == "s":
                del libros[id]
                print("Eliminado correctamente.")
            else:
                print("Operación cancelada.")
            break  # salimos del bucle después de encontrar el libro
    else:
        print("No se encontró un libro con ese ID.")

def salir():
    print("Saliendo...")

while True:
    menu()
    opc= input("Ingrese una opcion: ")
    match opc:
        case "1":
            añador_libro()
        case "2":
            consultar_libro()
        case "3":
            modificar_libro()
        case "4":
            eliminar_libro()
        case "5":
            salir()
            break
        case _: 
            print("Ingrese una opcion correcta")