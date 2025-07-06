# Enunciado 2: Inventario Simple de Productos 
# Descripción: Este sistema permite gestionar un inventario básico de productos. Cada producto tendrá un ID único, un nombre, un precio y una cantidad en stock. El sistema permitirá agregar, consultar, actualizar y eliminar productos.

# Características Clave: 
# •	Uso de un diccionario donde las claves son los IDs de los productos y los valores son diccionarios con los detalles del producto. 

# •	Generación automática de ID para los productos. 

# •	Funciones para cada operación. 

# •	Validación de entradas numéricas y existencia de productos. 

# •	Ciclos y decisiones para la lógica del programa. 

lista= []


def Menu():
    print("1- Agregar producto")
    print("2- Consultar producto")
    print("3- Actualizar producto")
    print("4- Eliminar producto")
    print("5- Salir")


def Agregar_producto():
    nombre= input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad en stock del producto: "))
    
    id = len(lista) + 1 ##Aumenta el id
    
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    lista.append(producto)
    print("Producto agregado correctamente")

def Consultar_producto():
    enontrado = False
    id = int(input("Ingrese el ID del producto que desea consultar: "))
    
    for producto in lista:
        if producto["id"] == id:
            print(f"ID: {producto['id']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']:.2f}")
            print(f"Stock: {producto['stock']}")
            enontrado = True
            break
    if not enontrado:
        print("Producto no encontrado")

def Actualizar_producto():
    pass

def Eliminar_producto():
    pass

def Salir():
    pass

while True:
    Menu()
    opc = input("Ingrese una opcion: ")
    
    match opc:
        case "1":
            Agregar_producto()
        case "2":
            Consultar_producto()
        case "3":
            Actualizar_producto()
        case "4":
            Eliminar_producto()
        case "5":
            Salir()
            break
        case _:
            print("Ingrese una opcion correcta ")
