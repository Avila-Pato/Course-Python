# Enunciado 2: Inventario Simple de Productos
# Descripción: Este sistema permite gestionar un inventario básico de productos. Cada producto tendrá un ID único, un nombre, un precio y una cantidad en stock. El sistema permitirá agregar, consultar, actualizar y eliminar productos.

# Características Clave:
# •	Uso de un diccionario donde las claves son los IDs de los productos y los valores son diccionarios con los detalles del producto.

# •	Generación automática de ID para los productos.

# •	Funciones para cada operación.

# •	Validación de entradas numéricas y existencia de productos.

# •	Ciclos y decisiones para la lógica del programa.

lista = []


def Menu():
    print("1- Agregar producto")
    print("2- Consultar producto")
    print("3- Actualizar producto")
    print("4- Eliminar producto")
    print("5- Salir")


def Agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad en stock del producto: "))

    id = len(lista) + 1  ##Aumenta el id

    producto = {"id": id, "nombre": nombre, "precio": precio, "stock": stock}
    lista.append(producto)
    print("Producto agregado correctamente")


def Consultar_producto():

    if not lista:
        print("No hay prudoctos que ver")
        return

    id = int(input("Ingrese el ID del producto que desea consultar: "))
    enontrado = False
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

    if not lista:
        print("No hay productos para ver")
        return

    try:
        idx = int(input("Ingrese el número del contacto que desea modificar: "))
    except:
        print("ID invalido")

    for producto in lista:
        if producto["id"] == idx:
            print(f"ID", producto["id"])
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']:.2f}")
            print(f"Stock: {producto['stock']}")

            print("Ingrese los neuvos datos")
            producto["nombre"] = input("Nombre: ")
            try:
                producto["precio"] = float(input("Precio: "))
                producto["stock"] = int(input("Stock: "))
            except:
                print("Error al ingresar los datos ")

            print("Contacto modificado correctamamente")


def Eliminar_producto():

    if not lista:
        print("No hay productos para ver")
        return

    idx = int(input("Ingrese la id que desea borrar: "))

    for producto in lista:
        if producto["id"] == idx:
            print(f"Id", producto["id"])
            print(f"Nombre", producto["nombre"])
            print(f"Precio", producto["precio"])
            print(f"Stock", producto["stock"])
    confirmar = input("Esta seguro que desea elimianrlo?(s/n): ")

    if confirmar == "s":
        # del producto["id"]
        producto["id"] == idx
        lista.remove(producto)  ##()
        print("Producto eliminado correctamtene")
    else:
        print("Producto cancelado")


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
